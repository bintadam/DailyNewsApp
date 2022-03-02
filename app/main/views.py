from flask import render_template, request, redirect, url_for
from  .views import *
from  . import main
from  ..request import *

@main.route('/')
def root():

    return redirect(url_for('main.sources'))

@main.route('/sources')
def sources():
    
    title = 'sources'
    news_sources = get_sources('general')
    sports_sources = get_sources('sports')
    health_sources = get_sources('health')
    business_sources = get_sources('business')
    
    return render_template('index.html', title=title, news=news_sources, sports=sports_sources, health=health_sources, business=business_sources)


@main.route('/articles/<source>')
def articles(source):
    articles = get_articles(source)
    return render_template('news.html, title=source, articles=articles')