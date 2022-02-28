from flask import render_template, request, redirect, url_for
from  .views import *
from  . import main
from ..request import *

@m.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title)


@app.route('/news/<int:news_id>')
def news(news_id):
    
    
    '''
    View news page function that returns the news details page and its data
    '''
    title = 'Home - Welcome to the best News Review Website online'
    return render_template('news.html',id = news_id)
