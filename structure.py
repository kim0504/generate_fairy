import gradio as gr
import ui, func, initial
import openai

openai.api_key = initial.api_key

ex_fairy = [{"image":"","title":"제목입니다", "content":"내용입니다"},
            {"image":"","title":"제목입니다", "content":"내용입니다"},
            {"image":"","title":"제목입니다", "content":"내용입니다"},
            {"image":"","title":"제목입니다", "content":"내용입니다"},
            {"image":"","title":"제목입니다", "content":"내용입니다"}]

with gr.Blocks() as demo:

    """ state """
    state = gr.State(initial.initial_state)
    state_chatbot = gr.State([])

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

    globals()['new_btn'].click(func.move_new_list, [], pages)
    globals()['load_btn'].click(func.move_load_list, [], pages)

    home_btn = [value for key, value in globals().items() if key.endswith('home_btn')]
    m_new_select_btn = [(key, value) for key, value in globals().items() if key.startswith('new_list_select_btn')]
    select_btn = [value for key, value in globals().items() if key.startswith('new_select_btn')]
    load_select_btn = [value for key, value in globals().items() if key.startswith('load_list_select_btn')]

    for btn in home_btn:
        btn.click(func.move_init,
                  [],
                  pages)

    for key,btn in m_new_select_btn:
        btn.click(func.move_new,
                  [state, state_chatbot, gr.State(initial.system_msg_3pig), gr.State(key[-1])],
                  [state, state_chatbot] + select_btn + pages)

    for btn in select_btn:
        btn.click(func.generate,
                  [state, state_chatbot, btn],
                  [state, state_chatbot, globals()['new_content']]+select_btn+[globals()['new_img']])

    for btn in load_select_btn:
        pass
        # btn.click(func.move_load, [], pages)








if __name__ == "__main__":
    demo.launch()