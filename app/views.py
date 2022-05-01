from email import message
from turtle import title
from flask import render_template
from app import app

@app.route('/')
def index():
  """
  Root page function
  """

  title = 'Home - The  best parting shot news website'
  return render_template('index.html', title = title)

@app.route('/science/<int:science_id>')
def science(science_id):

    '''
    View science news page function that returns the science news page and its data
    '''
    title = 'Science news from around the world'
    return render_template('science.html', title = title)