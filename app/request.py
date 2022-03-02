import json
from urllib import request
from .models import Article, Source


# Getting api key
ARTICLES = None
# Getting the movie base url
SOURCES = None

def configure_request(app):
    global ARTICLES, SOURCES
    ARTICLES = app.config['ARTICLES']
    SOURCES = app.config['SOURCES']


def get_articles(source):
    path = ARTICLES.format(source)
    content = request.urlopen(path)
    jason = json.loads(content.read())
    return jason ['articles']


def process_articles(articles):
    my_articles = []
    for each in articles:
        a = articles(
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
    path = SOURCES.format(category)
    content = request.urlopen(path)
    jason = json.loads(content.read())
    return jason['sources']        


def process_articles(sources):
    my_sources = []
    for s in sources :
        s = sources(
          s['id'],
          s['name'],
          s['description'],
          s['url'],
          s['language']
        )

        my_sources.append(s)
        return my_sources