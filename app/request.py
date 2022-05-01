from app import app
import urllib.request,json
from .models import *



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