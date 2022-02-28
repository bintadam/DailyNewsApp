from app import app
import urllib.request,json 
from models import article
from models import source

def get_articles(source):
    path = article.format(source)
    content = request.urlopen(path)
    jason = jason.loads(content.read())
    return jason ['articles']