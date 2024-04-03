# Text-to-Speech and Speech-to-Text Flask App

A Flask application that provides text-to-speech and speech-to-text functionality.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Project Structure](#project-structure)

## Installation

1. Clone the repository:
git clone https://github.com/aryasadawrate19/TTS-STT.git

2. Navigate to the project directory:
cd TTS-STT

3. Create and activate a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


4. Install the required dependencies:
pip install -r requirements.txt

## Usage

1. Run the Flask application:
flask run

2. Open your web browser and navigate to `http://localhost:5000`.

3. Follow the instructions on the web page to use the text-to-speech and speech-to-text functionalities.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.


## Project Structure

- `app.py`: The Flask application file that defines the routes and handles the app logic.
- `text_to_speech.py`: This module contains the text-to-speech functionality.
- `speech_to_text.py` (to be added): This module will handle the speech-to-text functionality.
- `templates/base.html`: The base HTML template that other templates extend.
- `templates/index.html`: The home page template with links to text-to-speech and speech-to-text.
- `templates/text_to_speech.html`: The template for the text-to-speech functionality.
- `templates/speech_to_text.html`: The template for the speech-to-text functionality

