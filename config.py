import os

class Config:
    '''
    General configuration parent class
    '''
    MY_API_KEY = os.environ.get('MY_API_KEY')

    MY_NEWS_BASE_URL ='https://newsapi.org'
    ARTICLES ='https://newsapi.org/v2/everything?sources={}&apikey=' + str(MY_API_KEY)
    SOURCES = 'https://newsapi.org/v2/top-headlines/sources?category={}&apikey=' + str(MY_API_KEY)

 
    pass



class ProdConfig(Config):
    
    pass


class DevConfig(Config):
   
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}
