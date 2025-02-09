from datetime import datetime
from blog import db

class User(db.Model):
    __tablename__ = 'user'      # not necessary, default value is 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    imageFile = db.Column(db.String(20), nullable = False, default='default.jpg')
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.imageFile})"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    datePosted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.datePosted}')"
