from src.DATA.msg import * 
from src.DATA.prompts import Dic as dic 
from Email.email import email_prompts
from src.CONVERSATION.tts import speak 
from src.BRAIN.chat import send_to_ai  , chat_bot
from src.FUNCTION.Email_send import send_email 
from src.FUNCTION.incog import incog_mode , open_chrome_incognito , open_firefox_private
from src.FUNCTION.youtube_downloader import download_video 
from src.FUNCTION.news import news_headlines 
from src.FUNCTION.weather import get_weather_report
from src.FUNCTION.random_respon import random_choice 
from src.VISION.eye import capture_image_and_save , detect_object 
from os import getcwd, system , environ 
from dotenv import load_dotenv
import webbrowser 
import platform
import time 


def ai_response(content_type: str) -> str:
    formatted_prompt = None 
    speak("working on it sir.")
    if content_type in ['story', 'song', 'summary' , 'joke']:
        placeholders = {}
        prompt_structure = dic[content_type]['prompt']
        for placeholder in prompt_structure.split('{')[1:]:
            placeholder_key = placeholder.split('}')[0]
            placeholders[placeholder_key] = input(f"Enter {placeholder_key.replace('_', ' ')}: ")
        formatted_prompt = prompt_structure.format(**placeholders)
        speak(random_choice(creative_responses))
    
    elif content_type in ['youtube', 'instagram', 'github', 'youtube_trending']:
        speak(random_choice(loading_responses))
        time.sleep(0.1)
        webbrowser.open(dic[content_type]['prompt'])
        return
    
    elif content_type == 'weather':
        speak(random_choice(weather_responses))
        time.sleep(0.1)
        load_dotenv()
        api_key = environ.get('Weather_api')
        speak("Enter the name of city sir.")
        
        city = input("city name: ").strip().lower()
        report = get_weather_report(city , api_key)
        formatted_prompt = f"{dic[content_type]['prompt']} . {report}"
        
    
    elif content_type == 'news':
        load_dotenv()
        News_Api = environ.get("News_api")
        headlines = news_headlines(News_Api)
        if headlines:
            speak(random_choice(headlines_intro))
            time.sleep(0.01)
            for headline in headlines:
                print(headline)
                speak(headline)
                print("\n\n")
                time.sleep(0.00001)
        return 
                
                
        
    elif content_type in ['safari' , 'asphalt9' , 'chess']:
        formatted_prompt = dic[content_type]['prompt']
        speak(random_choice(app_loading_responses))
        time.sleep(0.1)
        system(f"open {formatted_prompt}")
        return 
    
    elif content_type == 'download_video':
        link = input("Enter the link: ")
        speak("wait for a minute working on it sir..")
        time.sleep(0.1)
        download_video(link, getcwd())
        return
    
    elif content_type == 'youtube_search':
        search = input("Search topic: ")
        speak(random_choice(searching_responses))
        time.sleep(0.1)
        webbrowser.open(dic[content_type]['prompt'].format(search=search))
        return
    
    elif content_type == 'incognito_mode':
        
        url = input("URL: ")
        speak(random_choice(private_mode_responses))
        time.sleep(0.1)
        if platform.system() == 'Windows':
            try:
                open_chrome_incognito(url)
            except Exception as e:
                print(e)
                
                try:
                    open_firefox_private(url)
                except Exception as e:
                    print(e)
        else:
            incog_mode(url)
            
        return
    
    elif content_type == 'vision':
        speak('put the object in front of camera')
        speak('you have 5 second')
        numeral = ['one' , 'two' , 'three' , 'four' , 'five']
        for i in range(5):
            speak(numeral[i])
            time.sleep(0.001)

        image_path = capture_image_and_save()
        print('...captured')
        result = detect_object(image_path)
        
    # Check if the content type is 'email'
    elif content_type == 'email':
        load_dotenv()
        SENDER_EMAIL = environ.get("Sender_email")
        RECIEVER_EMAIL = environ.get("Receiver_email")
        PASSWORD = environ.get("Password_email")
        
        # Get the template
        selected_template = input("Select an email template (job, friend, meeting, doctor, leave, product): ")
        if selected_template not in email_prompts:
            print("Invalid template selection.")
            return
        
        template = email_prompts[selected_template]
        placeholders = {}
        
        # Extract placeholders from the prompt
        for placeholder in template['prompt'].split('{')[1:]:
            placeholder_key = placeholder.split('}')[0]
            if placeholder_key not in placeholders:
                placeholders[placeholder_key] = input(f"Enter value for '{placeholder_key}': ")

        # Format the email prompt
        subject = template['role']
        formatted_prompt = template['prompt'].format(**placeholders)

        # Display the formatted email content
        print("----- Start prompt -----")
        print(formatted_prompt)
        print("----- End prompt -----")
        
        # Create the complete AI prompt
        formatted_prompt = f"{subject} . {formatted_prompt}"
        role = dic[content_type]['role']
        speak(random_choice(email_responses))
        time.sleep(0.1)
        response = send_to_ai(role , formatted_prompt)
        send_email(response , password=PASSWORD , receiver_email= RECIEVER_EMAIL , sender_email= SENDER_EMAIL)
        return 
    
    else:
        # if prompt is also in the text we try to extract that 
        data = content_type.split('+')
        
        if len(data) == 2:
            _ , intial_prompt = data 
        else:
            intial_prompt = "hey jarivs"
        
        speak(random_choice(chat_starting_responses))
        time.sleep(0.1)
        
        chat_bot(intial_prompt)
        return 
    # elif content_type == 'chat':
    #     speak(random_choice(chat_starting_responses))
    #     time.sleep(0.1)
    #     chat_bot()
    #     return 
    
    if formatted_prompt:
        role = dic[content_type]['role']
        print(f"{role} \n {formatted_prompt}\n")
        
        speak(random_choice(almost_done_responses))
        response = send_to_ai(role , formatted_prompt)
        return response 
