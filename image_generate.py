import openai
import requests

def get_translate(text):
    client_id = "9aaodRv2BMjg6IVHi913" # <-- client_id 기입
    client_secret = "WaDJ70ePfT" # <-- client_secret 기입

    data = {'text' : text,
            'source' : 'ko',
            'target': 'en'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)

def image_generate(msg):
    response = openai.Image.create(
      prompt=("A cartoon of "+msg),
      n=1,
      size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url

def describe(msg):
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': "Describe this content visually in one sentence."},
                  {'role': 'assistant', 'content': msg}]
    )
    described_msg: str = res['choices'][0]['message']['content']
    return described_msg

def generate_img(msg):
    trans = get_translate(msg)
    des = describe(trans)
    img = image_generate(des)
    return img
