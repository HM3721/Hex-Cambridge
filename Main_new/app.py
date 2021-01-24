from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, UserMixin
import sqlite3
from views.forms import LoginForm, SignupForm, ListingForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Education_Hex'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////D/HexCambridge/Hex-Cambridge/main/database/users.db'

#db = SQLAlchemy(app)
db = sqlite3.connect('users.db')
try:
    db.execute('CREATE TABLE Users (id INTEGER, fname TEXT, lname TEXT, email TEXT, password TEXT)')
    db.commit()
except sqlite3.OperationalError: 
    None

#class User(UserMixin):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(15), unique=True)
#    email = db.Column(db.String(50), unique=True)
#    password = db.Column(db.String(80))

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return db.query.get(int(id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def homepage():
    return render_template('index.html')


@app.route('/browse')
def browse():
    return render_template('listing.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/details')
def details():
    return render_template('details.html')

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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(firstname=form.fname.data,lastname=form.lname.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('New user has been created!')
        return render_template('index.html')
    
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)