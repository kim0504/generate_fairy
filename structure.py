import gradio as gr
import ui, func, initial, firebase
import openai

openai.api_key = initial.api_key

with gr.Blocks(css="./css.css") as demo:

    """ state """
    state = gr.State(initial.initial_state) #gpt 초기 설정
    state_chatbot = gr.State([]) #챗봇 초기 설정


    """ ui """
    with gr.Column() as init: #초기 화면
        globals().update(ui.init_dis())

    with gr.Column(visible=False) as new_list: #동화 생성 리스트
        globals().update(ui.new_list_dis(firebase.get_default()))

    with gr.Column(visible=False) as user_set: #동화 세팅
        globals().update(ui.new_setting_dis())

    with gr.Column(visible=False) as new: #동화 생성
        globals().update(ui.new_dis())

    with gr.Column(visible=False) as load_list: #저장된 동화 리스트
        globals().update(ui.load_list_dis(firebase.get_save()))

    with gr.Column(visible=False) as load: #저장된 동화
        globals().update(ui.load_dis())


    """ func """
    pages = [init, new_list, user_set, new, load_list, load] #화면 변수 리스트

    globals()['new_btn'].click(func.move_new_set, [], pages) #동화 세팅 화면으로 이동
    globals()['load_btn'].click(func.move_load_list, [], pages) #저장된 동화 리스트 화면으로 이동
    globals()['set_btn'].click(func.move_new_list, [globals()['set_radio'], globals()['set_slider']], pages) #동화 생성 리스트 화면으로 이동

    home_btn = [value for key, value in globals().items() if key.endswith('home_btn')] #각 화면에 있는 홈 버튼
    m_new_select_btn = [(key, value) for key, value in globals().items() if key.startswith('new_list_select_btn')] #동화 선택 버튼
    select_btn = [value for key, value in globals().items() if key.startswith('new_select_btn')] #선택지 버튼
    load_select_btn = [(key, value) for key, value in globals().items() if key.startswith('load_list_select_btn')] #동화 선택 버튼
    change_columns = [globals()['new_select_col'], globals()['new_save_col']] #선택지, 저장 버튼

    for btn in home_btn: #각 화면에 있는 홈 버튼 클릭
        btn.click(func.move_init,
                  [],
                  pages)

    for key,btn in m_new_select_btn: #새 동화 생성 리스트에 있는 동화 선택 버튼
        btn.click(func.move_new,
                  [state, state_chatbot, gr.State(key[-1])],
                  [state, state_chatbot, globals()['new_content'], globals()['new_img'], globals()['audio']] + select_btn + pages)

    for btn in select_btn: #새 동화 생성 화면에 있는 선택지 버튼
        btn.click(func.generate,
                  [state, state_chatbot, btn],
                  change_columns + [state, state_chatbot, globals()['new_content']]+select_btn+[globals()['new_img'], globals()['audio']])

    for key,btn in load_select_btn: #저장된 동화 리스트에서 동화 선택 버튼
        btn.click(func.move_load,
                  gr.State(key[-1]),
                  [globals()['load_img'], globals()['load_content']]+pages)

    globals()['new_save_btn'].click(func.save) #동화 저장(새 동화 만들기 마지막 분기)

    load_btns = [globals()['load_prev_btn'], globals()['load_prev_btn']] #불러운 동화 화면에 있는 앞,뒤 이동 버튼
    globals()['load_prev_btn'].click(func.load_prev_content, [], [globals()['load_img'], globals()['load_content']]) #앞 내용으로 이동
    globals()['load_next_btn'].click(func.load_next_content, [], [globals()['load_img'], globals()['load_content']]) #뒤 내용으로 이동

if __name__ == "__main__":
    demo.launch()