import gradio as gr
import openai
import json
import os
from PIL import Image
import requests
from io import BytesIO
import initial, image_generate
import audio_generate as audio
import firebase

count = 1

genre = ''
degree = 0.8

load_fairy = {}
load_page = 0
load_select_idx = 0

temp_image = []
generate_info = {"title": "",
                 "abstract": "",
                 "content": []}


def generate_select(state, state_chatbot, idx):
    global generate_info, degree
    """save func"""
    generate_info['title'] = firebase.fairy_dict[idx]['title']
    generate_info['abstract'] = firebase.fairy_dict[idx]['abstract']
    generate_info['content'].append(firebase.fairy_dict[idx]['content'])

    """gpt func"""
    messages = state + [{
        'role': 'user',
        'content': "\n".join([firebase.fairy_dict[idx]['content'], genre, initial.select_prompt])
    }]
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=degree
    )
    msg = res['choices'][0]['message']['content']
    new_state = [{
        'role': 'user',
        'content': firebase.fairy_dict[idx]['content']
    }, {
        'role': 'assistant',
        'content': msg
    }]
    state = state + new_state
    state_chatbot = state_chatbot + [(firebase.fairy_dict[idx]['content'], msg)]

    img = image_generate.generate_img(firebase.fairy_dict[idx]['content'])
    temp_image.append(img)

    """select func"""
    textbox = firebase.fairy_dict[idx]['content']
    msg = [m.strip() for m in msg.split("p")[1:] if m.strip()]

    filename = audio.generate([textbox]+msg)

    return state, state_chatbot, textbox, img, filename, *msg,

def generate(state, state_chatbot, text):
    global count
    if count<initial.count:
        messages = state + [{
            'role': 'user',
            'content': "\n".join([text, genre, initial.prompt, initial.select_prompt])
        }]
    else:
        messages = state + [{
            'role': 'user',
            'content': "\n".join([text, initial.prompt])
        }]
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=degree
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

    count += 1
    if count<=initial.count:
        select = msg.split("p")
        msg = select[0]
        select = [m.strip() for m in select[1:]]
        img = image_generate.generate_img(msg)
        generate_info['content'].append(msg)
        temp_image.append(img)
        filename = audio.generate([msg] + select)
        return gr.update(visible=True), gr.update(visible=False), state, state_chatbot, msg, *select, img, filename
    else:
        select = ["end" for i in range(4)]
        img = image_generate.generate_img(msg)
        generate_info['content'].append(msg)
        temp_image.append(img)
        filename = audio.generate([msg])
        return gr.update(visible=False), gr.update(visible=True), state, state_chatbot, msg, *select, img, filename

def save():
    fairy = firebase.get_save()
    os.mkdir(f"./save_image/{len(fairy)}")
    for idx,img in enumerate(temp_image):
        res = requests.get(img)
        get_img = Image.open(BytesIO(res.content))
        get_img.save(f"./save_image/{len(fairy)}/{idx}.jpg")
    firebase.save(generate_info)

def load_prev_content():
    global load_page
    load_page -= 1
    return image_generate.open("/".join([initial.save_image_path, load_select_idx, f"{load_page}.jpg"])), load_fairy['content'][load_page]

def load_next_content():
    global load_page
    load_page += 1
    return image_generate.open("/".join([initial.save_image_path, load_select_idx, f"{load_page}.jpg"])), load_fairy['content'][load_page]

def move_init():
    return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def move_new_list(radio, slider):
    global genre, degree
    genre, degree = radio, slider
    if not genre=="선택 안함":
        genre = f'{genre}를 주제로,'
    return gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def move_new_set():
    return gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def move_new(state, state_chatbot, idx):
    aaa = generate_select(state, state_chatbot, idx)
    return *aaa, gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)

def move_load_list():

    return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)

def move_load(idx):
    global load_fairy, load_select_idx
    load_fairy = firebase.get_save()[idx]
    load_select_idx = idx
    return image_generate.open("/".join([initial.save_image_path, idx, "0.jpg"])), load_fairy['content'][0], gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)