import gradio as gr
import openai
import initial, image_generate

count = 1
genre = ''
degree = 1
full_content = []

def generate_select(state, state_chatbot, idx):
    global full_content
    full_content.append(initial.fairy_dict[idx]['content'])
    messages = state + [{
        'role': 'user',
        'content': "\n".join([initial.fairy_dict[idx]['content'], initial.select_prompt])
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
    msg = [m.strip() for m in msg.split("p")[1:] if m.strip()]

    return state, state_chatbot, *msg

def generate(state, state_chatbot, text):
    global count, full_content
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
        full_content.append(msg)
        select = [m.strip() for m in select[1:]]
        img = image_generate.generate_img(msg)
        return gr.update(visible=True), gr.update(visible=False), state, state_chatbot, msg, *select, img
    else :
        select = ["end" for i in range(4)]
        full_content.append(msg)
        img = image_generate.generate_img(msg)
        return gr.update(visible=False), gr.update(visible=True), state, state_chatbot, msg, *select, img

def save():
    file = '../ai_internship/save.txt'
    with open(file, 'a', encoding='UTF8') as f:
        f.write(full_content)

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
    print(aaa)
    return *aaa, gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)

def move_load_list():
    return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)

def move_load():
    return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)