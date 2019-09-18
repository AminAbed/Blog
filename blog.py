from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
# In order to use session in flask you need to set the secret key in your application settings.
# SECRET_KEY is a random key used to encrypt your cookies and save send them to the browser.
app.config['SECRET_KEY'] = '8f9940aec084fcfa3c9cda754bf619d2'

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


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="0.0.0.0", port=5000, debug=True)