import pyttsx3 as tts

engine = tts.init()

def text_to_speech_exec(text):
    engine.say(text)
    engine.runAndWait()
