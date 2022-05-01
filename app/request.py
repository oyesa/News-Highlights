from app import app
import urllib.request,json
from .models import Article, Source



# Getting news api key
api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']

def get_article_top_headlines(category):
  get_articles_url = base_url.format(category, api_key)
  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data = url.read()
    get_articles_response = json.loads(get_articles_data)

    articles_results = None

    if get_articles_response['articles']:
      articles_results_list = get_articles_response['articles']
      articles_results = process_results(articles_results_list)

      return articles_results

def process_results(articles_list):
  '''
  Function that processes articles results and transforms it to a list of objects
  '''
  articles_results = []
  for article in articles_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publisheAt')
        content = article.get('content')
        
        if urlToImage:
            article_object = Article(author,title,description,url,urlToImage,publishedAt,content)
            articles_results.append(article_object)

  return articles_results
  