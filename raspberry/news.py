import requests, json

# From https://newsapi.org

apiKey = "db597713532b42f8a87a98487954b034"

baseUrl = "https://newsapi.org/v1/articles"

source = "bbc-news"

def getNewsString():
    return "Here are the latest titles from BBC News: {} . That is all for the news today. ".format(getHeadlines())

def getHeadlines():
    articles = getArticles()

    headlines = ""

    for article in articles:
        headlines += article['title']
        headlines += ". "

    return headlines.encode('ascii', 'ignore').decode('ascii')

def getArticles():
    responseJSON = getRequestJSON(url)

    return responseJSON['articles']

def getUrl():
    return baseUrl + '?source=' + source + '&apiKey=' + apiKey

def getRequestJSON(url):
    response  = requests.get(url)
    return response.json()
