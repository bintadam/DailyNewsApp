import urllib.request,json 
from models import article
from models import source


# Getting api key
MY_API_KEY = None
# Getting the movie base url
MY_BASE_URL = None

def configure_request(app):
    global MY_API_KEY,MY_BASE_URL
    MY_API_KEY = app.config['MY_API_KEY']
    MY_BASE_URL = app.config['MY_BASE_URL']


def get_articles(source):
    path = MY_API_KEY.format(source)
    content = request.urlopen(path)
    jason = jason.loads(content.read())
    return jason ['articles']


def process_articles(articles):
    my_articles = []
    for each in articles:
        a = article(
            each['source'],
            each['title'],
            each['author'],
            each['urlToImage'],
            each['url'],
            each['publishedAt'],
            each['description'],
            each['content'],   
        )
        my_articles.append(a)
        return my_articles


def get_sources(category):
    path = MY_BASE_URL.format(category)
    content = request.urlopen(path)
    jason = jason.loads(content.read())
    return jason['source']        


def process_articles(sources)
    my_sources = []
    for s in sources    
        s = sources(
          s['id'],
          s['name'],
          s['description'],
          s['url'],
          s['language']
        )

        my_sources.append(s)
        return my_sources