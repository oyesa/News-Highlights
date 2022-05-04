class Article:
  '''
  article and source class to define article and source objects
  '''

  def __init__(self, author,title, description, url, urlToImage, publishedAt, content):
     self.author = author
     self.title = title
     self.description = description
     self.url = url
     self.urlToImage = urlToImage
     self.publishedAt = publishedAt
     self.content = content


class Source:

 def __init__(self, id, name, description, url, category, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
