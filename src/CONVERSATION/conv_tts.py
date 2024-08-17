import pyttsx3
from textblob import TextBlob

emotion_keywords = {
    "ecstatic": ['ecstatic'],
    "overjoyed": ['overjoyed'],
    "elated": ['elated'],
    "joyful": ['joyful'],
    "happy": ['happy'],
    "cheerful": ['cheerful'],
    "content": ['content'],
    "pleased": ['pleased'],
    "neutral": ['neutral'],
    "indifferent": ['indifferent'],
    "unhappy": ['unhappy'],
    "sad": ['sad'],
    "mournful": ['mournful'],
    "despondent": ['despondent'],
    "melancholy": ['melancholy'],
    "depressed": ['depressed'],
    "devastated": ['devastated'],
    "hopeful": ['hopeful'],
    "optimistic": ['optimistic'],
    "grateful": ['grateful'],
    "inspired": ['inspired'],
    "amused": ['amused'],
    "calm": ['calm'],
    "confused": ['confused'],
    "disappointed": ['disappointed'],
    "frustrated": ['frustrated'],
    "anxious": ['anxious'],
    "overwhelmed": ['overwhelmed'],
    "guilty": ['guilty'],
    "disgusted": ['disgusted'],
    "repulsed": ['repulsed'],
    "detached": ['detached']
}

def detect_emotion(text):
    text_lower = text.lower()
    for emotion, keywords in emotion_keywords.items():
        if any(word in text_lower for word in keywords):
            return emotion
    return "unknown"



def get_emotion(sentiment , BASE_SPEED = 130  , BASE_VOLUME = 1.0):
    if sentiment > 0.7:
        return "ecstatic", (BASE_SPEED + 55 , BASE_VOLUME + 0.5)
    elif 0.6 <= sentiment <= 0.7:
        return "overjoyed", (BASE_SPEED + 45 , BASE_VOLUME + 0.4)
    elif 0.5 <= sentiment < 0.6:
        return "elated", (BASE_SPEED + 40, BASE_VOLUME + 0.3)
    elif 0.4 <= sentiment < 0.5:
        return "joyful", (BASE_SPEED + 30, BASE_VOLUME + 0.2)
    elif 0.3 <= sentiment < 0.4:
        return "happy", (BASE_SPEED + 20, BASE_VOLUME + 0.1)
    elif 0.2 <= sentiment < 0.3:
        return "cheerful", (BASE_SPEED + 10, BASE_VOLUME)
    elif 0.1 <= sentiment < 0.2:
        return "content", (BASE_SPEED + 5 , BASE_VOLUME - 0.1)
    elif 0.05 <= sentiment < 0.1:
        return "pleased", (BASE_SPEED, BASE_VOLUME - 0.2)
    elif -0.05 <= sentiment < 0.05:
        return "neutral", (BASE_SPEED - 5, BASE_VOLUME)
    elif -0.1 <= sentiment < -0.05:
        return "indifferent", (BASE_SPEED - 10, BASE_VOLUME)
    elif -0.2 <= sentiment < -0.1:
        return "unhappy", (BASE_SPEED - 20, BASE_VOLUME)
    elif -0.3 <= sentiment < -0.2:
        return "sad", (BASE_SPEED - 30, BASE_VOLUME)
    elif -0.4 <= sentiment < -0.3:
        return "mournful", (BASE_SPEED - 40, BASE_VOLUME)
    elif -0.5 <= sentiment < -0.4:
        return "despondent", (BASE_SPEED - 50, BASE_VOLUME)
    elif -0.6 <= sentiment < -0.5:
        return "melancholy", (BASE_SPEED - 60, BASE_VOLUME - 0.1)
    elif -0.7 <= sentiment < -0.6:
        return "depressed", (BASE_SPEED - 70, BASE_VOLUME - 0.2)
    elif sentiment <= -0.7:
        return "devastated", (BASE_SPEED - 80, BASE_VOLUME - 0.3)
    elif 0.5 <= sentiment < 0.6:
        return "hopeful", (BASE_SPEED + 40, BASE_VOLUME + 0.3)
    elif 0.4 <= sentiment < 0.5:
        return "optimistic", (BASE_SPEED + 30, BASE_VOLUME + 0.2)
    elif 0.3 <= sentiment < 0.4:
        return "grateful", (BASE_SPEED + 20, BASE_VOLUME + 0.1)
    elif 0.2 <= sentiment < 0.3:
        return "inspired", (BASE_SPEED + 10, BASE_VOLUME)
    elif 0.1 <= sentiment < 0.2:
        return "amused", (BASE_SPEED + 5 , BASE_VOLUME - 0.1)
    elif 0.05 <= sentiment < 0.1:
        return "calm", (BASE_SPEED, BASE_VOLUME - 0.2)
    elif -0.05 <= sentiment < 0.05:
        return "confused", (BASE_SPEED - 10, BASE_VOLUME - 0.2)
    elif -0.1 <= sentiment < -0.05:
        return "disappointed", (BASE_SPEED - 20, BASE_VOLUME - 0.1)
    elif -0.2 <= sentiment < -0.1:
        return "frustrated", (BASE_SPEED - 30, BASE_VOLUME - 0.5)
    elif -0.3 <= sentiment < -0.2:
        return "anxious", (BASE_SPEED - 40, BASE_VOLUME - 0.2)
    elif -0.4 <= sentiment < -0.3:
        return "overwhelmed", (BASE_SPEED - 50, BASE_VOLUME)
    elif -0.5 <= sentiment < -0.4:
        return "guilty", (BASE_SPEED - 60, BASE_VOLUME)
    elif -0.6 <= sentiment < -0.5:
        return "disgusted", (BASE_SPEED - 70, BASE_VOLUME)
    elif -0.7 <= sentiment < -0.6:
        return "repulsed", (BASE_SPEED - 80, BASE_VOLUME)
    elif sentiment <= -0.7:
        return "detached", (BASE_SPEED - 90, BASE_VOLUME - 0.2)




def convSpeak(text):
    try:
        engine = pyttsx3.init()
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        #print(sentiment)
        emotion, (adjusted_rate, adjusted_volume) = get_emotion(sentiment)
        #print(emotion)
        # Adjust speech characteristics based on emotion
        engine.setProperty('rate', adjusted_rate)
        engine.setProperty('volume', adjusted_volume)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[14].id)

        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(e)
        pass



