from src.BRAIN.embd import similar_prompt 
from src.BRAIN.nltk_embd import nltk_sim_prompt
from src.CONVERSATION.speech import recognize_speech 
from src.response import ai_response 
from src.CONVERSATION.conv_tts import convSpeak 
from src.FUNCTION.random_respon import random_choice 
from src.DATA.msg import responses , welcome_responses , end_responses , ending_phrases
import time 


def main():
    print("[*] Say 'hey jarvis' to activate, or 'exit' to quit.")
    listening_mode = False
    
    while True:
        #time.sleep(0.5)
        spoken_text = recognize_speech()
        #time.sleep(0.5)
        if spoken_text:
            print(f"You said: {spoken_text}")

            if "hey jarvis" in spoken_text.lower() and not listening_mode:
                convSpeak("Hello Mr. Stark.")
                convSpeak(random_choice(welcome_responses))
                print("Listening mode activated.")
                listening_mode = True
            
            elif any(phrase in spoken_text.lower() for phrase in ending_phrases) and listening_mode:
            # elif "exit" in spoken_text.lower():
                convSpeak(random_choice(end_responses))
                listening_mode = False
                print("Exiting...")
                break
            
            elif listening_mode:
                prompt = spoken_text.strip()
                
                try:
                    content_type = similar_prompt(prompt)
                except Exception as e:
                    print("Install and start lm studio..")
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
