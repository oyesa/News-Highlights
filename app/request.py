import urllib.request
import json
from .models import Article, Source



api_key = ''
base_url = None
base_url_source = None


def configure_request(app):
  
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    base_url_source = app.config['NEWS_API_SOURCE_URL']
    
    pass

def get_articles(source_id):
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=44524a2a935b40d0ba2fef55f93001b5'.format(source_id)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)
    return articles_results


def get_articles_from_source_selected(source, pageLimitSize):
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=44524a2a935b40d0ba2fef55f93001b5&pageSize={}'.format(source, pageLimitSize)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)
    return articles_results


def get_articles_depending_on_category_of_the_source(category):
    get_articles_url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey=44524a2a935b40d0ba2fef55f93001b5'.format(category)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)
    return articles_results

def get_source(): 
    get_source_url = 'https://newsapi.org/v2/sources?apiKey=44524a2a935b40d0ba2fef55f93001b5'.format()
    print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results_sources(source_results_list)

    return source_results


def process_results(articles_list):
  articles_results = []
  for article in articles_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        
        if urlToImage:
            article_object = Article(author,title,description,url,urlToImage,publishedAt,content)
            articles_results.append(article_object)

  return articles_results

def process_results_sources(source_list):
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')

        source_object = Source(
            id, name, description, url, category, language)
        source_results.append(source_object)

    return source_results
