from flask import Flask, redirect, url_for, render_template, request, session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "EduMenu"
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes = 10)

db = SQLAlchemy(app)

class users(db.Model):
    email = db.Colum("email", db.string(100))
    password = db.Colum("password", db.string(100))

def __init__(self, email, password):
    self.email = email
    self.password = password

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["Email"]
        session["user"] = user
        found_user = users.query.filter_by(email=user).first()

        if found_user:
            session["password"] = founder_user.password

        else:
            urs = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash ("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session :
            flash ("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods = ["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(email=user).first()
            found_user.password = password
            db.session.commit()
            flash ("Email was saved")
        else:
            if "password" in session:
                password = session["password"]
        return render_template("user.html", password = password)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
flash("You have been logged out!", "info")
session.pop("email", None)
session.pop("password", None)
return redirect(url_for("login"))

@app.route('/browse')
def browse():
    return render_template('list.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/details')
def details():
    return render_template('details.html')

if __name__ == "__main__":
    de.create_all()
    app.run(debug = True)
