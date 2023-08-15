from gtts import gTTS

def generate(content_list:list):
    tts = gTTS(text="\n".join(content_list), lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    return filename