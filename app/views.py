from email import message
from turtle import title
from flask import render_template, request, redirect, url_for
from app import app
from .request import get_article_top_headlines

#views
@app.route('/')
def index():
  """
  view root page function
  """
  business_articles = get_article_top_headlines('business')
  all_articles = get_article_everything('all')
  return render_template('index.html', all_articles = all_articles, business_articles = business_articles)

@app.route('/localnews')
def localnews():
  localnews_articles = get_article_everything('localnews')
  return render_template('localnews.html', localnews = localnews)

@app.route('/technology')
def technology():
  technology_articles = get_article_top_headlines('technology')
  return render_template('tech.html', technology = technology)

@app.route('/worldnews')
def worldnews():
  worldnews_articles = get_article_everything('world')
  return render_template('worldnews.html', worldnews = worldnews)