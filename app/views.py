from email import message
from turtle import title
from flask import render_template
from app import app
from .request import get_article_top_headlines

@app.route('/')
def index():
  """
  view root page function
  """
  business_articles = get_article_top_headlines('business')
  print(business_articles)
  title = 'Home - The  best parting shot news website'
  return render_template('index.html', title = title, business_articles = business_articles)

@app.route('/science/<int:science_id>')
def science(science_id):

    '''
    View science news page function that returns the science news page and its data
    '''
    title = 'Science news from around the world'
    return render_template('science.html', title = title)