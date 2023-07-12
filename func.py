import gradio as gr
import openai
import initial, image_generate

count = 1

def generate_select(state, state_chatbot, text, idx):
    idx=int(idx)
    messages = state + [{
        'role': 'user',
        'content': "\n".join([text[idx], initial.assis_msg_3pig])
    }]
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )
    msg: str = res['choices'][0]['message']['content']
    new_state = [{
        'role': 'user',
        'content': text[idx]
    }, {
        'role': 'assistant',
        'content': msg
    }]
    state = state + new_state
    state_chatbot = state_chatbot + [(text[idx], msg)]
    # print(msg.split("p"))
    msg = msg.split("p")
    del msg[0]
    msg = [m.strip() for m in msg if m.strip()]
    return state, state_chatbot, *msg

def generate(state, state_chatbot, text):
    # global count
    # count=count+1
    # if count==initial.end_count:
    messages = state + [{
        'role': 'user',
        'content': "\n".join([text, initial.prompt, initial.assis_msg_3pig])
    }]
    # else:
    #     messages = state + [{
    #         'role': 'user',
    #         'content': "\n".join([text, initial.prompt])
    #     }]
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
    # if count==initial.end_count:
    #     select = ["end" for i in range(4)]
    #     trans = image_generate.get_translate(msg)
    #     des = image_generate.describe(trans)
    #     img = image_generate.image_generate(des)
    #     return state, state_chatbot, msg, *select, img
    # else :
    select = msg.split("p")
    msg = select[0]
    del select[0]
    select = [m.strip() for m in select]
    trans = image_generate.get_translate(msg)
    des = image_generate.describe(trans)
    img = image_generate.image_generate(des)
    print(state)
    print(state_chatbot)
    print(msg)
    print("select", len(select), select)
    return state, state_chatbot, msg, *select, img

def change_btn():
    return gr.update(visible=True), gr.update(visible=False)

def move_init():
    return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def move_new_list():
    return gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def move_new(state, state_chatbot, text, idx):
    aaa = generate_select(state, state_chatbot, text, idx)
    return *aaa, gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)

def move_load_list():
    return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)

def move_load():
    return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)