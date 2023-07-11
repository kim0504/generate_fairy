import gradio as gr
import ui, func

ex_fairy = [{"image":"","title":"제목입니다", "content":"내용입니다"},
            {"image":"","title":"제목입니다", "content":"내용입니다"},
            {"image":"","title":"제목입니다", "content":"내용입니다"},
            {"image":"","title":"제목입니다", "content":"내용입니다"},
            {"image":"","title":"제목입니다", "content":"내용입니다"}]

with gr.Blocks() as demo:

    """ ui """
    with gr.Column() as init:
        globals().update(ui.init_dis())

    with gr.Column(visible=False) as new_list:
        globals().update(ui.new_list_dis(ex_fairy))

    with gr.Column(visible=False) as new:
        globals().update(ui.new_dis())

    with gr.Column(visible=False) as load_list:
        globals().update(ui.load_list_dis(ex_fairy))

    with gr.Column(visible=False) as load:
        globals().update(ui.load_dis())



    """ func """

    pages = [init, new_list, new, load_list, load]

    home_btn = [key for key, value in globals().items() if key.endswith('home_btn')]
    for btn in home_btn:
        globals()[btn].click(func.move_init, [], pages)

    new_select_btn = [key for key, value in globals().items() if key.startswith('new_list_select_btn')]
    for btn in new_select_btn:
        globals()[btn].click(func.move_new, [], pages)

    load_select_btn = [key for key, value in globals().items() if key.startswith('load_list_select_btn')]
    for btn in load_select_btn:
        globals()[btn].click(func.move_load, [], pages)

    select_btn = [key for key, value in globals().items() if key.startswith('new_select_btn')]
    for btn in select_btn:
        pass

    globals()['new_list_select_btn1'].click(func.move_new, [], pages)
    globals()['load_list_select_btn1'].click(func.move_load, [], pages)

    globals()['new_btn'].click(func.move_new_list, [], pages)
    globals()['load_btn'].click(func.move_load_list, [], pages)



if __name__ == "__main__":
    demo.launch()