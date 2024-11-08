# views.py is where the URLs root pages stored homePage, loginPgae, contactPage etc.

from flask import Blueprint, render_template

from flask_login import  login_required, current_user 


views = Blueprint('views',__name__)

@views.route('/')
def base():
  return render_template("base.html",user=current_user)

@views.route('/About')
def about():
  return render_template("about.html",user=current_user)
  