# Voice Assistant 'Jarvic'

**Jarvic** is a Python-based voice assistant that uses speech recognition and text-to-speech technologies to execute commands and interact with users. The assistant can navigate to websites and provide the latest news headlines based on voice commands.

## Features

- **Voice Activation**: Start the assistant by saying "Jarvis".
- **Web Navigation**: Open popular websites including Google, Facebook, LinkedIn, and YouTube.
- **News Retrieval**: Fetch and read out top news headlines using the News API.
- **Speech Output**: Verbal responses using the `pyttsx3` text-to-speech engine.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/<your-username>/Voice-Assistant-Jarvic.git
    cd Voice-Assistant-Jarvic
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Requirements

- Python 3.x
- `speech_recognition`
- `pyttsx3`
- `requests`
- `webbrowser`

## API Key

You need an API key from [NewsAPI](https://newsapi.org/) to fetch news headlines. Replace the placeholder API key in the script with your own.

## Usage

1. **Run the script:**

    ```bash
    python jarvic.py
    ```

2. **Interact with the assistant:**
   - Say "Jarvis" to activate the assistant.
   - Provide commands like "open Google", "open Facebook", or "news" to perform actions.

## Example

```plaintext
Listening for activation word...
Heard word: Jarvis
Jarvis Active....
Heard command: open Google
