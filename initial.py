import firebase

"""gpt initial state"""
api_key = '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' #please fill in this part

initial_state = [{'role': 'system', 'content': 'Act as a kindergarten teacher who reads fairy tales.'}]

prompt = '내용에 대해 150글자 내외 분량의 후속 이야기를 작성하고'

select_prompt = f'이 내용 뒤에 이어질 만한 4개의 선택지를 다음의 지시사항에 따라 만들어줘.\n' \
                 ' - 각각의 선택지를 한 줄로 제시해.\n' \
                 ' - 답변 예시: p1.셋째 돼지는 형 집에 얹혀살기로 했어요 p2.셋째 돼지는 집시 생활을 하기로 했어요 p3.셋째 돼지는 부모님 집에 얹혀살기로 했어요 p4.셋째 돼지는 아무생각이 없어요'

end_prompt = '내용에 대한 150글자 내외 분량의 후속 이야기를 작성하고 선택지를 제시하지 않고, 결말을 내줘'

count=4 #선택 횟수 설정


"""firebase initial state"""
firebase_json = "ai-internship-233e8-firebase-adminsdk-lswyx-ee1169e2c5.json" #please fill in this part
firebase_url = "https://ai-internship-233e8-default-rtdb.firebaseio.com/" #please fill in this part


"""local image"""
image_path = "./image"
save_image_path = "./save_image"