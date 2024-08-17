Dic = {
    'story':{
        'role': "You are the storyteller, tasked with creating captivating tales",
        'prompt': "Write a {genre} story about {character} in {setting}. Describe their journey and the challenges they face."
    },  
    'song':{
        'role': "You are the songwriter, weaving lyrics for various genres and themes",
        'prompt':"Compose lyrics for a {genre} song titled '{title}'. Focus on {emotion} and the theme of {theme}. How does the chorus reflect the overall {mood} of the song?"
    },
    'summary':{
        'role': "As the summarizer, your skill lies in creating concise and informative summaries",
        'prompt': "Generate a summary for the following {type} titled '{title}'. Provide a brief overview of the given {text} and mention any notable insights. Ensure the summary is around {length} words."
    },
    'news':{
        'role':"as a new reporter , what are todays news headlines",
        'prompt':""
    },
    'joke': {
        'role': "You are the joke teller, providing humorous content",
        'prompt': "Tell a {type_of_humor} joke about {topic} that is should be less than 50 words and suitable for an adult audience. Ensure the joke is engaging, funny , and tailored to mature tastes."
    },
    'youtube':{
        'role': "Execute the task of opening YouTube in the browser",
        'prompt': "https://www.youtube.com"
    },
    'download_video':{
        'role': "Your role is to download a YouTube video from a given link",
        'prompt':""
    },
    'vision':{
        'role':"what is this or tell me about the image . describe the given image",
        'prompt':""
    },
    'instagram':{
        'role': "Initiate the task of opening Instagram in the browser",
        'prompt': "https://www.instagram.com"
    },
    'safari':{
        'role': "Perform the action of opening the Safari browser",
        'prompt': "/Applications/safari.app"
    },
    'asphalt9':{
        'role': "Your role involves opening the Asphalt 9 game",
        'prompt': "/Applications/Asphalt9.app"
    },
    'chess':{
        'role': "Your responsibility is to open the chess game",
        'prompt': "/System/Applications/Chess.app"
    },
    'github':{
        'role': "Your role is to open the GitHub website",
        'prompt': "https://github.com"
    },
    'youtube_trending':{
        'role': "Open the YouTube trending page",
        'prompt': "https://www.youtube.com/feed/trending"
    },
    'youtube_search':{
        'role': "Perform a search on the YouTube website",
        'prompt': "https://www.youtube.com/results?search_query={search}"
    },
    'incognito_mode':{
        'role': "Initiate the task of opening chrome in incognito mode",
        'prompt':""
    },
    'email':{
        'role': "You are a professional email writer. Use a concise subject line. Write an email based on the provided content without altering any personal details",
        'prompt': ""
    },
    'weather':{   
        'role':"provide a brief summary of the current weather conditions",
        'prompt':"Using the provided weather data, summarize the current weather conditions in less than 40 words without using any numerical values"
    },
    'chat':{
        'role':"start the chat with ai",
        'prompt':"{intial_prompt}"
    }
}
