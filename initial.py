api_key = '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'

genre = ''

system_msg_3pig = ['아기 돼지 삼형제가 살았어요. 하루는 엄마 돼지가 말했지요.\n' \
                  ' 얘들아, 이제 너희는 다 컸다. 나가서 집을 지어 살려무나.\n' \
                  ' 첫째 돼지는 노는 걸 좋아했지요.\n' \
                  ' 하루종일 빈둥빈둥 놀다가 짚으로 후다닥 집을 지었어요.\n' \
                  ' 둘째 돼지는 먹는 걸 좋아했어요.\n' \
                  ' 하루종일 냠냠 쩝쩝 먹다가 나무로 후다닥 집을 지었어요.\n' \
                  ' 셋째 돼지는 어떤 선택을 할까요?']

assis_msg_3pig = f' - 장르는 {genre}로,\n' \
                 '다음의 지시사항에 따라 4개의 선택지를 만들어줘.\n' \
                 ' - 각각의 선택지를 한 줄로 제시해.\n' \
                 ' - 답변 예시: p1.셋째 돼지는 형 집에 얹혀살기로 했어요 p2.셋째 돼지는 집시 생활을 하기로 했어요 p3.셋째 돼지는 부모님 집에 얹혀살기로 했어요 p4.셋째 돼지는 아무생각이 없어요)'


initial_state = [{'role': 'system', 'content': 'Act as a kindergarten teacher who reads fairy tales.'}]

prompt = '내용에 대한 150글자 내외 분량의 후속 이야기를 작성하고 그에 대한 선택지를'

end_prompt = '내용에 대한 150글자 내외 분량의 후속 이야기를 작성하고 선택지를 제시하지 않고, 결말을 내줘'

end_count=4 #최대 선택 횟수

count=0 #선택 횟수