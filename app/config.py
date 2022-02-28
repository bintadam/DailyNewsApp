class Config:
    '''
    General configuration parent class
    '''
    MY_API_KEY = 
    MY_NEWS_BASE_URL ='https://newsapi.org'
    ARTICLES ='https://newsapi.org/v2/everything?sources={}&apikey=' + str(MY_API_KEY)
    SOURCES = 'https://newsapi.org/v2/top-headlines/sources?category={}apikey=' + str(MY_API_KEY)

 
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


