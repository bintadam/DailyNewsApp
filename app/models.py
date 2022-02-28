class article :
    '''
     class articles to define article Objects
    '''

    def __init__(self,source,title,author,urlToImage,url,publishedAt,description,content):
        self.source = source
        self.title = title
        self.author = author
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt = publishedAt
        self.description = description
        self.content = content


class source:
    '''
    source class to define source 
    '''

    def __init__(self,id,name,description,url,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.language = language        