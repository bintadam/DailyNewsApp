from flask import render_template, request, redirect, url_for
from  .views import *
from  . import main
from ..request import *

@main.route('/')
def root():

    return redirect(url_for('main.sources'))

@main.route('/sources')
def sources():
    
    title = 'sources'
    sports_sources = get_sources('sports')
    worklife_sources = get_sources('worklife')
    travel_sources = get_sources('travel')
    culture_sources = get_sources('culture')
    
    return render_template('index.html', title=title, sports=sports_sources, worklife=worklife_sources, travel=travel_sources, culture=culture_sources)


@main.route('/articles/<source>')
def articles(source):
    articles = get_articles(source)
    return render_template('news.html, title=source, articles=articles')