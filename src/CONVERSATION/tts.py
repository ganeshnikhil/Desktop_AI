
#pip3  install pyobjc==9.0.1

import pyttsx3

def speak(text):
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Set the speaking rate
        try:
            rate = engine.getProperty('rate')
            engine.setProperty('rate', 153)  # Setting up a new speaking rate
        except Exception as e:
            print(f"Error setting rate: {e}")

        # Set the volume
        try:
            volume = engine.getProperty('volume')
            engine.setProperty('volume', 1.0)  # Setting volume level between 0 and 1
        except Exception as e:
            print(f"Error setting volume: {e}")

        # Set the voice
        try:
            voices = engine.getProperty('voices')
            if len(voices) > 14:  # Check if the index is valid
                engine.setProperty('voice', voices[14].id)  # Set the voice by index
            else:
                print("Voice index out of range.")
        except Exception as e:
            print(f"Error setting voice: {e}")

        # Speak the text
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Error speaking text: {e}")
        finally:
            engine.stop()

    except Exception as e:
        print(f"Error initializing TTS engine: {e}")
