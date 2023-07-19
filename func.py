import gradio as gr
import openai
import json
import initial, image_generate

count = 1

genre = ''
degree = 1

generate_info = {"image": [],
                 "title": "",
                 "abstract": "",
                 "content": []}


def generate_select(state, state_chatbot, idx):
    global generate_info
    """save func"""
    generate_info['title'] = initial.fairy_dict[idx]['title']
    generate_info['abstract'] = initial.fairy_dict[idx]['abstract']
    generate_info['content'].append(initial.fairy_dict[idx]['content'])

    """gpt func"""
    messages = state + [{
        'role': 'user',
        'content': "\n".join([initial.fairy_dict[idx]['content'], initial.prompt, initial.select_prompt])
    }]
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )
    msg = res['choices'][0]['message']['content']

    new_state = [{
        'role': 'user',
        'content': initial.fairy_dict[idx]['content']
    }, {
        'role': 'assistant',
        'content': msg
    }]
    state = state + new_state
    state_chatbot = state_chatbot + [(initial.fairy_dict[idx]['content'], msg)]

    """select func"""
    textbox = initial.fairy_dict[idx]['content']
    msg = [m.strip() for m in msg.split("p")[1:] if m.strip()]

    return state, state_chatbot, textbox, *msg

def generate(state, state_chatbot, text):
    global count
    if count<initial.end_count:
        messages = state + [{
            'role': 'user',
            'content': "\n".join([text, initial.prompt, initial.select_prompt])
        }]
    else:
        messages = state + [{
            'role': 'user',
            'content': "\n".join([text, initial.end_prompt])
        }]
    print(f"text : {text}")
    print(messages)
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )
    msg = res['choices'][0]['message']['content']
    print(f"msg {msg}")
    new_state = [{
        'role': 'user',
        'content': text
    }, {
        'role': 'assistant',
        'content': msg
    }]
    state = state + new_state
    state_chatbot = state_chatbot + [(text, msg)]

    count += 1
    if count<=initial.end_count:
        select = msg.split("p")
        msg = select[0]
        generate_info['content'].append(msg)
        select = [m.strip() for m in select[1:]]
        img = image_generate.generate_img(msg)
        return gr.update(visible=True), gr.update(visible=False), state, state_chatbot, msg, *select, img
    else:
        select = ["end" for i in range(4)]
        generate_info['content'].append(msg)
        img = image_generate.generate_img(msg)
        return gr.update(visible=False), gr.update(visible=True), state, state_chatbot, msg, *select, img

def save():
    with open('./save_fairy.json', 'r', encoding='UTF8') as f:
        jso = json.load(f)

        jso[str(len(jso))] = generate_info

    with open('./save_fairy.json', 'w', encoding='UTF8') as f:
        json.dump(jso, f, indent=2, ensure_ascii=False)

def next_content(image, text):
    pass

def prev_content(image, text):
    pass

def move_init():
    return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def move_new_list(radio, slider):
    global genre, degree
    genre, degree = radio, slider
    return gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def move_new_set():
    return gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def move_new(state, state_chatbot, idx):
    aaa = generate_select(state, state_chatbot, idx)
    return *aaa, gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)

def move_load_list():
    return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)

def move_load():
    return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)