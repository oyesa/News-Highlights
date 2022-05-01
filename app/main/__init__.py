from flask import Blueprint
main = Blueprint('main',__name__)

#Import views and error files 
from app.main import views,error