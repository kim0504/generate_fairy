import gradio as gr
import initial, func
def init_dis():
    logo = gr.Image()
    with gr.Row():
        new_btn = gr.Button("New")
        load_btn = gr.Button("Load")
        option_btn = gr.Button("Option")
    return locals()

def new_list_dis(fairy_list):
    new_list_home_btn = gr.Button("Home")
    for idx,fairy in enumerate(fairy_list):
        with gr.Row():
            locals()[f'new_list_img{idx}'] = gr.Image()
            with gr.Column():
                locals()[f'new_list_title{idx}'] = gr.Textbox(fairy['title'])
                locals()[f'new_list_content{idx}'] = gr.Textbox(fairy['content'])
            locals()[f'new_list_select_btn{idx}'] = gr.Button("선택")
    return locals()

def new_setting_dis():
    set_radio = gr.Radio(['선택 안함', '로맨스', '공포', '판타지'])
    set_slider = gr.Slider(label="자유도")
    set_btn = gr.Button("완료")
    return locals()

def new_dis():
    new_home_btn = gr.Button("Home")
    with gr.Row():
        new_img = gr.Image()
        new_content = gr.Textbox(value=initial.system_msg_3pig[0], lines=10)

    new_select_col = gr.Column()
    with new_select_col:
        with gr.Row():
            new_select_btn_1 = gr.Button("1")
            new_select_btn_2 = gr.Button("2")
        with gr.Row():
            new_select_btn_3 = gr.Button("3")
            new_select_btn_4 = gr.Button("4")

    new_save_col = gr.Column(visible=False)
    with new_save_col:
        new_save_btn = gr.Button("Save")

    return locals()

def load_list_dis(fairy_list):
    load_list_home_btn = gr.Button("Home")
    for idx,fairy in enumerate(fairy_list):
        with gr.Row():
            locals()[f'load_list_img{idx}'] = gr.Image()
            with gr.Column():
                locals()[f'load_list_title{idx}'] = gr.Textbox(fairy['title'])
                locals()[f'load_list_content{idx}'] = gr.Textbox(fairy['content'])
            locals()[f'load_list_select_btn{idx}'] = gr.Button("선택")
    return locals()

def load_dis():
    load_home_btn = gr.Button("Home")
    with gr.Row():
        load_prev_btn = gr.Button("이전")
        load_img = gr.Image()
        load_content = gr.Textbox()
        load_next_btn = gr.Button("다음")
    return locals()