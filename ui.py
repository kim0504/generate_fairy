import gradio as gr
import initial, image_generate

def init_dis():
    logo = gr.Image(image_generate.open("/".join([initial.image_path, "logo.jpg"])), height=620, show_label=False, container=False, interactive=False)
    with gr.Row():
        gr.HTML()
        new_btn = gr.Button(value="New", show_label=False, container=False, scale=2)
        gr.HTML()
        load_btn = gr.Button("Load", show_label=False, container=False, scale=2)
        gr.HTML()
    return locals()

def new_setting_dis():
    with gr.Column(scale=10):
        gr.HTML()
    with gr.Row():
        with gr.Column(scale=1):
            gr.HTML()
        with gr.Column(scale=2):
            set_radio = gr.Radio(choices=['선택 안함', '로맨스', '공포', '판타지'], label="장르 선택")
            set_slider = gr.Slider(label="자유도 설정", maximum=2, show_label="자유도 설정")
            with gr.Row():
                gr.HTML()
                set_btn = gr.Button("완료")
                gr.HTML()
        with gr.Column(scale=1):
            gr.HTML()
    with gr.Column(scale=1):
        gr.HTML()
    return locals()

def new_list_dis(fairy_list):
    new_list_home_btn = gr.Button("Home", elem_id="warning")
    for key,val in fairy_list.items():
        with gr.Row():
            locals()[f'new_list_img{key}'] = gr.Image(image_generate.open("/".join([initial.image_path, f"{val['title']}.jpg"])), height=300, show_label=False, container=False)
            with gr.Column():
                locals()[f'new_list_title{key}'] = gr.Textbox(val['title'], show_label=False, container=False)
                gr.HTML()
                locals()[f'new_list_content{key}'] = gr.Textbox(val['abstract'], lines=9,show_label=False, container=False)
            locals()[f'new_list_select_btn{key}'] = gr.Button("선택", show_label=False)
    return locals()

def new_dis():
    new_home_btn = gr.Button("Home")
    with gr.Row():
        new_img = gr.Image(height=400, show_label=False, container=False)
        new_content = gr.Textbox(value="", lines=17, show_label=False, elem_id="fairy-content")

    new_select_col = gr.Column()
    with new_select_col:
        with gr.Row():
            new_select_btn_1 = gr.Button("0")
            new_select_btn_2 = gr.Button("2")
        with gr.Row():
            new_select_btn_3 = gr.Button("3")
            new_select_btn_4 = gr.Button("4")

    new_save_col = gr.Column(visible=False)
    with new_save_col:
        new_save_btn = gr.Button("Save")

    with gr.Row():
        with gr.Column(scale=1):
            gr.HTML()
        with gr.Column(scale=2):
            audio = gr.Audio(container=False, show_label=False)
        with gr.Column(scale=1):
            gr.HTML()

    return locals()

def load_list_dis(fairy_list):
    load_list_home_btn = gr.Button("Home")
    for key,val in fairy_list.items():
        with gr.Row():
            with gr.Column(scale=1):
                locals()[f'load_list_img{key}'] = gr.Image(image_generate.open("/".join([initial.save_image_path,key,"0.jpg"])), height=300, show_label=False, container=False)
            with gr.Column(scale=2):
                with gr.Column():
                    locals()[f'load_list_title{key}'] = gr.Textbox(val['title'], show_label=False, container=False)
                    gr.HTML()
                    locals()[f'load_list_content{key}'] = gr.Textbox(val['abstract'], show_label=False, container=False)
            with gr.Column(scale=1):
                locals()[f'load_list_select_btn{key}'] = gr.Button("선택")
    return locals()

def load_dis():
    load_home_btn = gr.Button("Home")
    with gr.Row():
        with gr.Column(scale=1):
            gr.HTML()
        with gr.Column(scale=7):
            with gr.Row():
                load_img = gr.Image(show_label=False, container=False)
                load_content = gr.Textbox(lines=16, show_label=False, elem_id="fairy-content")
        with gr.Column(scale=1):
            gr.HTML()
    with gr.Row():
        with gr.Column(scale=1):
            load_prev_btn = gr.Button("이전")
        with gr.Column(scale=2):
            gr.HTML()
        with gr.Column(scale=1):
            load_next_btn = gr.Button("다음")
    return locals()