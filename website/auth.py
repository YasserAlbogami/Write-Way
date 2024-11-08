from flask import Blueprint, jsonify , render_template, request, flash, redirect, url_for
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user 
import json

auth = Blueprint('auth',__name__)

@auth.route('/Home',methods = ['GET','POST'])
@login_required
def home():
  if request.method == 'POST':
    note = request.form.get('note')
    
    if len(note) < 1:
      flash('Note is too short',category="Error")
    
    else:
      new_note = Note(data=note, user_id=current_user.id)
      db.session.add(new_note)
      db.session.commit()      
      flash('Note added!',category='success')
        
  
  return render_template("home.html",user=current_user)

@auth.route('/delete-note', methods = ['POST'])
def delete_note():
  note = json.loads(request.data)
  noteID = note['noteID']
  note = Note.query.get(noteID)
  
  if note:
    if note.user_id == current_user.id:
      db.session.delete(note)
      db.session.commit()
  
  return jsonify({})  

@auth.route('/log-in',methods = ['GET','POST'])
def Log_in():
  if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')

        user = User.query.filter_by(email=email).first()
        if user:
          
          if check_password_hash(user.password, str(password)):
              flash('Logged in successfully!', category='success')
              login_user(user,remember=True)
              return redirect(url_for('auth.home'))
              
              
          else:
                flash('Incorrect password, try again.', category='Error')
        
        else:
          flash('Email does not exist.', category='Error')

  return render_template("log-in.html",user=current_user)

@auth.route('/log-out')
@login_required
def Log_out():
  logout_user()
  return redirect(url_for('auth.Log_in'))

@auth.route('/sign-up',methods = ['GET','POST'])
def Sign_up():
  if request.method == 'POST' :
    email = request.form.get('email')
    first_name = request.form.get('FirstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    
    user = User.query.filter_by(email=email).first()
    
    if user:
      flash('There is a user with the provided email',category='Error')

    elif len(email) < 4:
      flash('Email is too short',category='Error')
      
    elif len(first_name) < 2:
      flash('First name is too short',category='Error')
    
    elif password1 != password2:
      flash('Passwords don\'t match', category='Error')
    
    elif len(str(password1)) < 7:
      flash('The password should be at least 7 digits', category='Error')
    
    elif (not hasUpperCase(str(password1))) : # yasser
      flash('The password doesn\'t contain any uppercase lettter', category='Error')

    else:
     new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1,method='pbkdf2:sha256'))
     db.session.add(new_user)
     db.session.commit()
     login_user(new_user,remember=True)
     flash('Account created Sucessfully', category='success') 
     return redirect(url_for('auth.home')) 
      
  return render_template('/sign-up.html',user=current_user) 


def hasUpperCase(password):
  return any(char.isupper() for char in password)