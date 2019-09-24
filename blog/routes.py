from flask import render_template, url_for, flash, redirect
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post
from blog import app

posts = [
    {
        'author':'author_1',
        'title':'Blog Post 1',
        'content':'Blog Post Content 1',
        'datePosted':'2019-09-11'
    },
    {
        'author':'author_2',
        'title':'Blog Post 2',
        'content':'Blog Post Content 2',
        'datePosted':'2018-09-11'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Home Page")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You are now logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful, please check email and password!" ,'danger')
        return redirect(url_for('login'))
    return render_template("login.html", title="Login", form=form)