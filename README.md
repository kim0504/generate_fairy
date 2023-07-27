### Interactice fairy generator

- **기간** : 2023.07
- **주제** : GPT api를 활용한 인터렉티브 창장 동화 생성
- **개발** : Python, GPT, Dalle2, Google tts, Papgo, Firebase, Gradio
- **Flow**
<p align="center"> 
  <img src="https://github.com/kim0504/generate_fairy/assets/81956540/ab4f58d9-68e2-4b93-a9e7-a717020c441c.jpg" width="70%" height="70%" align='center'/>
</p>

<br></br>
### How to use

- open api 발급

```python
#initial.py

openai_api_key = "<your key>"
```

- firebase 프로젝트 생성 후 json 파일 및 url 기입

```python
#initial.py

...
"""firebase initial state"""
firebase_json = "<json file>" #please fill in this part
firebase_url = "<firebase url>" #please fill in this part
...
```

- main.py 실행
<br></br>
### Content

- main.py
    - gradio 실행
<br></br>
- initial.py
    - 초기 값 설정
        - ChatGPT
        - Firebase
        - Local path
<br></br>
- audio_generate.py
    - google tts 기능으로 오디오 생성
<br></br>
- image_ngenerate.py
    - dalle2를 통한 이미지 생성
<br></br>
- structure.py
    - gradio 구성
<br></br>
- ui.py
    - gradio ui
<br></br>
- func.py
    - gradio function
<br></br>
- css.css
    - gradio component css
<br></br>
- fairy.json
    - 초기 동화 파일
