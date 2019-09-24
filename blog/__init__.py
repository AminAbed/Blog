from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# In order to use session in flask you need to set the secret key in your application settings.
# SECRET_KEY is a random key used to encrypt your cookies and save send them to the browser.
app.config['SECRET_KEY'] = '8f9940aec084fcfa3c9cda754bf619d2'
# specify the location of db '///' is a relative path from current folder 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# instantiate the db
db = SQLAlchemy(app)

from blog import routes