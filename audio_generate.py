from gtts import gTTS

def generate(content_list:list):
    name = "\n".join(content_list)
    tts = gTTS(text=name, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    return filename