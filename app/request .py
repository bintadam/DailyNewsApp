from app import app
import urllib.request,json 
from models import article
from models import source

def get_articles(source):
    path = article.format(source)
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