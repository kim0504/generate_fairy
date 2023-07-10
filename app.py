import gradio as gr
import openai

openai.api_key = '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'

a=0
def answer(state, state_chatbot, text):
    messages = state + [{
        'role': 'user',
        'content': text
    }]
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    msg = res['choices'][0]['message']['content']
    new_state = [{
        'role': 'user',
        'content': text
    }, {
        'role': 'fairy tale writer',
        'content': msg
    }]
    state = state + new_state
    state_chatbot = state_chatbot + [(text, msg)]

    return state, state_chatbot, state_chatbot




with gr.Blocks(css='#chatbot .overflow-y-auto{height:750px}') as demo:
    state = gr.State([{
        'role': 'system',
        'content': "아기 돼지 삼형제가 살았어요. 하루는 엄마 돼지가 말했지요.\"얘들아, 이제 너희는 다 컸다. 나가서 집을 지어 살려무나\".\n첫째 돼지는 노는 걸 좋아했지요. 하루종일 빈둥빈둥 놀다가 짚으로 후다닥 집을 지었어요.\n둘째 돼지는 먹는 걸 좋아했어요. 하루종일 냠냠 쩝쩝 먹다가 나무로 후다닥 집을 지었어요.\n셋째 돼지는 어떤 선택을 할까요?\n너는 소설가이고 이 다음에 올 선택지를 4개 제시해줘, 각각의 선택지는 한줄로 제시되어야해, 답변은 제시문으로만 작성해\n답변 예시 :\n1.셋째 돼지는 형 집에 얹혀살기로 했어요.\n2.셋째 돼지는 집시 생활을 하기로 했어요.\n3.셋째 돼지는 부모님 집에 얹혀살기로 했어요.\n4.셋째 돼지는 아무생각이 없어요."    }])
    state_chatbot = gr.State([])
    print(state)
    if a==0:
        str = "아기 돼지 삼형제가 살았어요. 하루는 엄마 돼지가 말했지요.\"얘들아, 이제 너희는 다 컸다. 나가서 집을 지어 살려무나.\"\n첫째 돼지는 노는 걸 좋아했지요. 하루종일 빈둥빈둥 놀다가 짚으로 후다닥 집을 지었어요.\n둘째 돼지는 먹는 걸 좋아했어요. 하루종일 냠냠 쩝쩝 먹다가 나무로 후다닥 집을 지었어요.\n셋째 돼지는 어떤 선택을 할까요?"
    else:
        str= "짜잔"
    with gr.Row():
        gr.HTML("""<div style="text-align: right; max-width: 500px; margin: 0 auto;">
            <div>
                <h1>Make Your Story ChatGPT-3.5</h1>
            </div>
            <p style="margin-bottom: 10px; font-size: 94%">
                team4 
            </p>
        </div>""")
    gr.Textbox(
        label="동화내용",
        info="Initial text",
        lines=3,
        value=str
    )
    with gr.Row():
        chatbot = gr.Chatbot(elem_id='chatbot')

    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder='Send a message...').style(container=False)



    txt.submit(answer, [state, state_chatbot, txt], [state, state_chatbot, chatbot])
    txt.submit(lambda: '', None, txt)
    a=1

demo.launch(debug=True, share=True)