import requests


def news_headlines(api_key , country='in' , top = 10):
    headlines = []
    url = ('https://newsapi.org/v2/top-headlines?'
        f'country={country}&'
        f'apiKey={api_key}')
    try:
        response = requests.get(url).json()
        all_articles = response['articles']
        total_results = int(response['totalResults'])
        for i in range(min(top , total_results)):
            headline = all_articles[i]['title']
            headlines.append(headline)
        return headlines
    except Exception as e:
        print(e)
        pass
    return None 


