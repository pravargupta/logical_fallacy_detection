# Logical Fallacy Detection

Building a project to detect fault logics in an argument/speech that sound like they make sense but are based off a wrong base overall and are very hard to find out in the heat of the moment.

For now we have speech to text recognition where we play audio from microphone and it outputs to output.txt(using google speech recognition) and then we run it through gemini api because gemini is free for educational use.

The text is then passed through gemini api with the prompt to detect fallacies within that text, this will be updated and made with a way better version in future too.

## Features

- **Speech-to-Text**: Converts live audio from the microphone to text using Google's Speech Recognition API.
- **Fallacy Detection**: The text is analyzed using the Gemini API to identify logical fallacies.
- **Planned Updates**: More advanced fallacy detection and better integration with future API versions.

## Requirements

- Python 3.12+
- Flask (for serving the app locally)
- Gemini API (for fallacy detection)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/pravargupta/logical_fallacy_detection.git
cd logical_fallacy_detection
```

### 2. Install Dependencies

Use `pip` to install the necessary libraries listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 3. Add Your Gemini API Key

Create a `.env` file in the root directory and add your **Gemini API** key. This key is required to access the fallacy detection service.

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the Application

Start the Flask server to run the application on your local machine.

```bash
python server.py
```

The application should now be running at `http://localhost:5000/`.

## Usage

1. **Speech Input**: Speak into the microphone. The system will capture your audio, convert it to text, and save it as `output.txt`.
2. **Fallacy Detection**: The text is processed using the Gemini API to detect any logical fallacies. The results are then displayed on the local server.

## Future Improvements

- Enhance fallacy detection using a more sophisticated AI model.
- Improve error handling and optimize real-time fallacy detection.
- Integrate additional APIs for better accuracy and a wider range of fallacy types.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
