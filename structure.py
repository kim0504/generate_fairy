import gradio as gr
import openai

ex_fairy = [{"image":"","title":"제목입니다", "content":"내용입니다"},
            {"image":"","title":"제목입니다", "content":"내용입니다"}]

with gr.Blocks() as demo:

    with gr.Column() as init:
        logo = gr.Image()
        with gr.Row():
            new_btn = gr.Button("New")
            load_btn = gr.Button("Load")
            option_btn = gr.Button("Option")

    with gr.Column(visible=False) as new_list:
        start_btn1 = gr.Button("Home")
        for fairy in ex_fairy:
            with gr.Row():
                fairy_image = gr.Image()
                with gr.Column():
                    fairy_title = gr.Textbox(fairy['title'])
                    fairy_content = gr.Textbox(fairy['content'])
                select_btn = gr.Button("선택")

    with gr.Column(visible=False) as load_list:
        start_btn1 = gr.Button("Home")
        for fairy in ex_fairy:
            with gr.Row():
                fairy_image = gr.Image()
                with gr.Column():
                    fairy_title = gr.Textbox(fairy['title'])
                    fairy_content = gr.Textbox(fairy['content'])
                select_btn = gr.Button("선택")

    with gr.Column(visible=False) as main:
        start_btn2 = gr.Button("Home")
        with gr.Row():
            img = gr.Image()
            content = gr.Textbox()
        with gr.Column():
            with gr.Row():
                btn1 = gr.Button("1")
                btn2 = gr.Button("2")
            with gr.Row():
                btn3 = gr.Button("3")
                btn4 = gr.Button("4")

    def move_main():
        return gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)

    def move_list():
        return gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)

    def move_init():
        return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)

    new_btn.click(move_list, [], [init, new_list, main])
    select_btn.click(move_main, [], [init, new_list, main])
    start_btn1.click(move_init, [], [init, new_list, main])
    start_btn2.click(move_init, [], [init, new_list, main])


if __name__ == "__main__":
    demo.launch()
