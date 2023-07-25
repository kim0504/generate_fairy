import json

api_key = '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'

initial_state = [{'role': 'system', 'content': 'Act as a kindergarten teacher who reads fairy tales.'}]

prompt = '내용에 대해 150글자 내외 분량의 후속 이야기를 작성하고'

select_prompt = f'이 내용 뒤에 이어질 만한 4개의 선택지를 다음의 지시사항에 따라 만들어줘.\n' \
                 ' - 각각의 선택지를 한 줄로 제시해.\n' \
                 ' - 답변 예시: p1.셋째 돼지는 형 집에 얹혀살기로 했어요 p2.셋째 돼지는 집시 생활을 하기로 했어요 p3.셋째 돼지는 부모님 집에 얹혀살기로 했어요 p4.셋째 돼지는 아무생각이 없어요)'

end_prompt = '내용에 대한 150글자 내외 분량의 후속 이야기를 작성하고 선택지를 제시하지 않고, 결말을 내줘'

end_count=4 #최대 선택 횟수

count=0 #선택 횟수

with open('./fairy.json', encoding='UTF8') as f:
    fairy_dict = json.load(f)

image_path = "./image"
save_image_path = "./save_image"