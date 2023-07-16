import gradio as gr
import openai
import initial, image_generate

count = 1
genre = ''
degree = 1
full_content = initial.assis_msg_3pig

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
    global count, full_content
    if count<initial.end_count:
        messages = state + [{
            'role': 'user',
            'content': "\n".join([text, initial.prompt, initial.assis_msg_3pig])
        }]
    else:
        messages = state + [{
            'role': 'user',
            'content': "\n".join([text, initial.end_prompt])
        }]
    count += 1

    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )
    msg = res['choices'][0]['message']['content']
    new_state = [{
        'role': 'user',
        'content': text
    }, {
        'role': 'assistant',
        'content': msg
    }]
    state = state + new_state
    state_chatbot = state_chatbot + [(text, msg)]
    if count<=initial.end_count:
        select = msg.split("p")
        msg = select[0]
        full_content = full_content + f"${msg}"
        select = [m.strip() for m in select[1:]]
        trans = image_generate.get_translate(msg)
        des = image_generate.describe(trans)
        img = image_generate.image_generate(des)
        return gr.update(visible=True), gr.update(visible=False), state, state_chatbot, msg, *select, img
    else :
        select = ["end" for i in range(4)]
        full_content = full_content+f"${msg}"
        print(full_content)
        trans = image_generate.get_translate(msg)
        des = image_generate.describe(trans)
        img = image_generate.image_generate(des)
        return gr.update(visible=False), gr.update(visible=True), state, state_chatbot, msg, *select, img

def next_content(image, text):
    pass

def prev_content(image, text):
    pass

def save_fairy():
    global full_content

def move_init():
    return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def move_new_list(radio, slider):
    global genre, degree
    genre, degree = radio, slider
    return gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def move_new_set():
    return gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def move_new(state, state_chatbot, text, idx):
    print(count, initial.end_count)
    aaa = generate_select(state, state_chatbot, text, idx)
    return *aaa, gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)

def move_load_list():
    return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)

def move_load():
    return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)