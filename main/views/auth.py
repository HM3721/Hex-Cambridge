from flask import Flask, render_template, redirect, url_for, request, Blueprint, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from main import db, login_manager
from .forms import LoginForm, SignupForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

    flash('Please check your login details and try again.')
    return render_template('login.html', form=form)
    #checking the user's email/password correct or not
    #email = request.form.get('email')
    #password = request.form.get('password')
    #remember = True if request.form.get('remember') else False

    #user = User.query.filter_by(email=emai).first()
    #user = User.query.filter_by(True).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    #if not user : #{or not check_password_hash(user.password, password)}:
        #flash('Please check your login details and try again.')
        #return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    #login_user(user, remember=remember)
    #login_user(user,True)
    #return redirect(url_for('main.profile'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(firstname=form.fname.data,lastname=form.lname.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('New user has been created!')
        return render_template('index.html')
    
    return render_template('signup.html', form=form)
    #checking the user's email/password correct or not
    #email = request.form.get('email')
    #name = request.form.get('name')
    #password = request.form.get('password')

    #user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    #user = User.query.filter_by(True).first() # if this returns a user, then the email already exists in database
    #if user: # if a user is found, we want to redirect back to signup page so user can try again
        #flash('Email address already exists')
        #return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    #new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    #db.session.add(new_user)
    #db.session.commit()

