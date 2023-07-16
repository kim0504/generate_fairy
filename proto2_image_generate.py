import gradio as gr
import openai
import requests

def get_translate(text):
    client_id = "9aaodRv2BMjg6IVHi913" # <-- client_id 기입
    client_secret = "WaDJ70ePfT" # <-- client_secret 기입

    data = {'text' : text,
            'source' : 'ko',
            'target': 'en'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)

def image_generate(msg):
    response = openai.Image.create(
      prompt=("A cartoon of "+msg),
      n=1,
      size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url

def describe(msg):
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': "Describe this content visually in one sentence."},
                  {'role': 'assistant', 'content': msg}]
    )
    described_msg: str = res['choices'][0]['message']['content']
    return described_msg

#openai.api_key = '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'
openai.api_key = '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'
system_msg_3pig = '아기 돼지 삼형제가 살았어요. 하루는 엄마 돼지가 말했지요.\n' \
                  ' 얘들아, 이제 너희는 다 컸다. 나가서 집을 지어 살려무나.\n' \
                  ' 첫째 돼지는 노는 걸 좋아했지요.\n' \
                  ' 하루종일 빈둥빈둥 놀다가 짚으로 후다닥 집을 지었어요.\n' \
                  ' 둘째 돼지는 먹는 걸 좋아했어요.\n' \
                  ' 하루종일 냠냠 쩝쩝 먹다가 나무로 후다닥 집을 지었어요.\n' \
                  ' 셋째 돼지는 어떤 선택을 할까요?'

assis_msg_3pig = '다음의 지시사항에 따라 4개의 선택지를 만들어줘.\n' \
                 ' - 각각의 선택지를 한 줄로 제시해.\n' \
                 ' - 답변 예시: p1. 셋째 돼지는 형 집에 얹혀살기로 했어요 p2.셋째 돼지는 집시 생활을 하기로 했어요 p3.셋째 돼지는 부모님 집에 얹혀살기로 했어요 p4.셋째 돼지는 아무생각이 없어요)'

initial_state = [
    {'role': 'system', 'content': 'Act as a kindergarten teacher who reads fairy tales.'},
    # {'role': 'assistant', 'content': system_msg_3pig},
    # {'role': 'user', 'content': assis_msg_3pig}]
    ]
prompt = '내용에 대한 150글자 내외 분량의 후속 이야기를 작성하고 그에 대한 선택지를 같은 형식으로 4개 제시해줘'
end_prompt = '내용에 대한 150글자 내외 분량의 후속 이야기를 작성하고 선택지를 제시하지 않고, 결말을 내줘'
end_count=4 #최대 선택 횟수
count=0 #선택 횟수
with gr.Blocks() as demo:

    """ 대화 저장 """
    state = gr.State(initial_state)
    state_chatbot = gr.State([])

    """ 위젯들 """
    start_btn = gr.Button("시작하기")
    with gr.Row():
        img = gr.Image()
        content = gr.Textbox(value=system_msg_3pig)
    with gr.Column():
        with gr.Row():
            btn1 = gr.Button("Next num")
            btn2 = gr.Button("Next num")
            btn_temp = gr.Button("Next num", visible=False)
        with gr.Row():
            btn3 = gr.Button("Next num")
            btn4 = gr.Button("Next num")

    def generate_select(state, state_chatbot, text):
        messages = state + [{
            'role': 'user',
            'content': "\n".join([text, assis_msg_3pig])
        }]
        res = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
        )
        msg: str = res['choices'][0]['message']['content']
        new_state = [{
            'role': 'user',
            'content': text
        }, {
            'role': 'assistant',
            'content': msg
        }]
        state = state + new_state
        state_chatbot = state_chatbot + [(text, msg)]
        #print(msg.split("p"))
        msg=msg.split("p")
        del msg[0]
        msg = [m.strip() for m in msg if m.strip()]
        return state, state_chatbot, *msg

    def generate(state, state_chatbot, text):
        global count
        count=count+1
        if count==end_count:
            messages = state + [{
                'role': 'user',
                'content': "\n".join([text, end_prompt])
            }]
        else:
            messages = state + [{
                'role': 'user',
                'content': "\n".join([text, prompt])
            }]

        res = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
        )
        msg:str = res['choices'][0]['message']['content']
        new_state = [{
            'role': 'user',
            'content': text
        }, {
            'role': 'assistant',
            'content': msg
        }]
        state = state + new_state
        state_chatbot = state_chatbot + [(text, msg)]
        if count==end_count:
            select = ["end" for i in range(4)]
            trans = get_translate(msg)
            des = describe(trans)
            img = image_generate(des)
            return state, state_chatbot, msg, *select, img
        else :
            select = msg.split("p")
            msg = select[0]
            del select[0]
            select = [m.strip() for m in select if m.strip()]
            trans = get_translate(msg)
            des = describe(trans)
            img = image_generate(des)
            return state, state_chatbot, msg, *select, img

    start_btn.click(generate_select,
               [state, state_chatbot, content],
               [state, state_chatbot, btn1, btn2, btn3, btn4])

    btn1.click(generate,
               [state, state_chatbot, btn1],
               [state, state_chatbot, content, btn1, btn2, btn3, btn4, img])

    btn2.click(generate,
               [state, state_chatbot, btn2],
               [state, state_chatbot, content, btn1, btn2, btn3, btn4, img])

    btn3.click(generate,
               [state, state_chatbot, btn3],
               [state, state_chatbot, content, btn1, btn2, btn3, btn4, img])

    btn4.click(generate,
               [state, state_chatbot, btn4],
               [state, state_chatbot, content, btn1, btn2, btn3, btn4, img])


if __name__ == "__main__":
    demo.launch()
