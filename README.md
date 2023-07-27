### Interactice fairy generator

- **기간** : 2023.07
- **주제** : GPT api를 활용한 인터렉티브 창장 동화 생성
- **개발** : Python, GPT, Dalle2, Google tts, Papgo, Firebase, Gradio
- **Flow**
    
    ![flow.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/57024978-4936-4852-9fff-f2b2f0ab3be8/flow.jpg)
    

### How to use

- open api 발급

```python
#initial.py

openai_api_key = "<your key>"
```

- firebase 프로젝트 생성
- main.py 실행

### Content

- main.py
    - gradio 실행
- initial.py
    - 초기 값 설정
        - 뭐뭐 있는 지
- audio_generate.py
    - google tts 기능으로 오디오 생성
- image_ngenerate.py
    - dalle2를 통한 이미지 생성
- structure.py
    - gradio 구성
- ui.py
    - gradio ui
- func.py
    - gradio function
- css.css
    - gradio component css
- fairy.json
    - 초기 동화 파일
```
