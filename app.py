import pyttsx3 as tts
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

engine = tts.init()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text-to-speech', methods=['GET', 'POST'])
def text_to_speech():
    if request.method == 'POST':
        text = request.form['text']
        engine.say(text)
        engine.runAndWait()
        return 'Text-to-speech conversion done!'
    return render_template('text_to_speech.html')

@app.route('/speech-to-text', methods=['GET', 'POST'])
def speech_to_text():
    # Add your speech-to-text functionality here
    pass

if __name__ == '__main__':
    app.run(debug=True)