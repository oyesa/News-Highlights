from flask import render_template
from ..request import get_articles, get_source, get_articles_from_source_selected, get_articles_depending_on_category_of_the_source
from . import main

#views
@main.route('/')
def index():
    sources = get_source()
    bbc_news = get_articles_from_source_selected('bbc-news', '8')
    aljazeera = get_articles_from_source_selected('al-jazeera-english', '8')
    cnn_home = get_articles_from_source_selected('cnn', '1')
    bbc_news_home = get_articles_from_source_selected('bbc-news', '2')
    cbc_news = get_articles_from_source_selected('cbc-news', '2')
    title = 'Home - Welcome to Parting Shot News'
    return render_template('index.html',title=title, bcc=bbc_news_home, bbc_news=bbc_news, cnn_home=cnn_home, sources=sources, cbc_news=cbc_news, aljazeera=aljazeera)


@main.route('/news-source/articles/<source_id>')
def articles(source_id):
    articles = get_articles(source_id)
    title = f'{source_id}'

    return render_template('articles.html', title=title, articles=articles)


@main.route('/localnews')
def localnews():
    localnews = get_articles_depending_on_category_of_the_source('localnews')
    title = 'News from Kenya to the world'
    return render_template('localnews.html',title=title,localnews=localnews)


@main.route('/business')
def business():
    business = get_articles_depending_on_category_of_the_source('business')
    title = 'Business news from around the world'
    return render_template('business.html',title=title,business=business)


@main.route('/worldnews')
def worldnews():
    worldnews = get_articles_depending_on_category_of_the_source(
        'worldnews')
    title = 'News from around the world'
    return render_template('worldnews.html', title=title, worldnews=worldnews)


@main.route('/health')
def health():
    health = get_articles_depending_on_category_of_the_source('health')
    title = 'News on health from all over world'
    return render_template('health.html', title=title, health=health)


@main.route('/technology')
def technology():
    technology = get_articles_depending_on_category_of_the_source('technology')
    title = 'News on technology from around the world'
    return render_template('tech.html',title=title, technology=technology)