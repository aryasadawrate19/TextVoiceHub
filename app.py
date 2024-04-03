from flask import Flask, render_template, request
from text_to_speech import text_to_speech_exec

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text_to_speech', methods=['GET', 'POST'])
def text_to_speech():
    if request.method == 'POST':
        text = request.form['text']
        text_to_speech_exec(text)
        return 'Text-to-speech conversion done!'
    return render_template('text_to_speech.html')

@app.route('/speech-to-text', methods=['GET', 'POST'])
def speech_to_text():
    # Speech-to-text functionality here
    pass

if __name__ == '__main__':
    app.run(debug=True)
