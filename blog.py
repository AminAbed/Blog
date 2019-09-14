from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="0.0.0.0", port=5000, debug=True)