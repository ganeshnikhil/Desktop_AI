


# Desktop AI Application

## Overview

This desktop AI application leverages advanced LLM models from LM Studio, along with various APIs for weather and news updates. It includes speech
recognition capabilities, cosine similarity for prompt comparison, and a range of responses for interactive communication.
The application is designed to be activated by voice commands and provides intelligent responses based on the context of the conversation.

## Features

- **Voice Activation**: Activate the AI with the command "Hey Jarvis".
- **Speech Recognition**: Converts spoken language into text.
- **Embedding and Similarity**: Uses embeddings to calculate cosine similarity between prompts and a list of predefined prompts.
- **API Integration**: Fetches data from weather and news APIs.
- **Dynamic Responses**: Provides varied responses based on the context of the conversation.

## Setup Instructions

### Prerequisites

- Python 3.9+ 
- Virtual Environment

### Setting Up the Virtual Environment

1. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ganeshnikhil/Desktop_AI.git
   cd Desktop_AI
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Create a `.env` file** in the root directory of the project.

2. **Add your API keys and other configuration variables** to the `.env` file. Here’s a sample structure:

   ```dotenv
   Weather_api=your_weather_api_key
   News_api=your_news_api_key
   Sender_email = your_email
   Receiver_email = subject_email
   Password_email = email_password.
   ```
3. **Setup the keys and passwords.
   
    [LMSTUDIO](https://lmstudio.ai)
    ```
       - Download llm models from lm studio these model run locally on your system.
         - nomic-embed-text-v1.5-GGUF (generate embeddings)
         - Mistral-7B-Instruct-v0.2-GGUF  (text model)
         - llava-phi-3-mini-gguf  (intall vision adapter)  (image + text) model
         - Eris_PrimeV4-Vision-32k-7B-GGUF-IQ-Imatrix  (install vision adapter) (image + text) model
    ````
    [WEATHER](https://rapidapi.com/weatherapi/api/weatherapi-com)
    ```
       - get weather api
    ```
    [NEWS](https://newsapi.org)
    ```
       - get news api
    ```
    [GMAIL_PASSWORD](https://myaccount.google.com/apppasswords)
    ```
       - generate password to send email using smptlib
    ```
5. **System requirements
    # higher is the specs better the model will perfomrm
   ```
    - 8gb+ ram (higher is better)
    - 250 gb+ storage 
    - i5 processor or m processor 
    - gpu / npu
   ```
  
   
### Usage

1. **Run the application**:

   ```bash
   python main.py
   ```

2. **Voice Commands**:

   - Say "Hey Jarvis" to activate listening mode.
   - Speak your prompt or query.
   - Say "exit" or use any of the ending phrases to terminate the session.

## Code

Here's a basic overview of the main code file:

```python
from src.BRAIN.embd import similar_prompt
from src.BRAIN.nltk_embd import nltk_sim_prompt
from src.CONVERSATION.speech import recognize_speech
from src.response import ai_response
from src.CONVERSATION.conv_tts import convSpeak
from src.FUNCTION.random_respon import random_choice
from src.DATA.msg import responses, welcome_responses, end_responses, ending_phrases
import time

def main():
    print("[*] Say 'hey jarvis' to activate, or 'exit' to quit.")
    listening_mode = False
    
    while True:
        spoken_text = recognize_speech()
        if spoken_text:
            print(f"You said: {spoken_text}")

            if "hey jarvis" in spoken_text.lower() and not listening_mode:
                convSpeak("Hello Mr. Stark.")
                convSpeak(random_choice(welcome_responses))
                print("Listening mode activated.")
                listening_mode = True
            
            elif any(phrase in spoken_text.lower() for phrase in ending_phrases) and listening_mode:
                convSpeak(random_choice(end_responses))
                listening_mode = False
                print("Exiting...")
                break
            
            elif listening_mode:
                prompt = spoken_text.strip()
                
                try:
                    content_type = similar_prompt(prompt)
                except Exception as e:
                    print("Install and start LM Studio..")
                    print(f"ERROR: {e}")
                    content_type = nltk_sim_prompt(prompt)
                    
                convSpeak(random_choice(responses))
                time.sleep(0.1)
                reaction = ai_response(content_type)
                if reaction:
                    print(reaction)
                    convSpeak(reaction)
            
if __name__ == "__main__":
    main()
```

## File Structure

- `src/`
  - `BRAIN/`
    - `embd.py`: Contains the `similar_prompt` function for cosine similarity.
    - `nltk_embd.py`: Contains the `nltk_sim_prompt` function for prompt similarity using NLTK.
  - `CONVERSATION/`
    - `speech.py`: Contains the `recognize_speech` function for speech recognition.
    - `conv_tts.py`: Contains the `convSpeak` function for text-to-speech conversion.
  - `response.py`: Contains the `ai_response` function to generate responses.
  - `FUNCTION/`
    - `random_respon.py`: Contains the `random_choice` function for selecting random responses.
  - `DATA/`
    - `msg.py`: Contains predefined response lists, including `responses`, `welcome_responses`, `end_responses`, and `ending_phrases`.

## License

This project is licensed under the GPL License - see the [LICENSE](https://github.com/ganeshnikhil/Desktop_AI/blob/main/LICENSE) file for details.

## Contributing

Feel free to submit issues, improvements, or pull requests. Please follow the standard guidelines for contributions.

## Contact

If you have any questions or need further assistance, please contact [ganeshnikhil124@gmail.com].
```
