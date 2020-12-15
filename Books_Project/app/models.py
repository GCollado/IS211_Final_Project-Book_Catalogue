from app import db, login
from flask_login import UserMixin
from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


# Defines User table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    book = db.relationship('Book', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# Defines and represents posts written by users
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(40))
    book_author = db.Column(db.String(20), nullable=False)
    page_total = db.Column(db.Integer, default=0)
    isbn10 = db.Column(db.Integer, default=None)
    isbn13 = db.Column(db.Integer, default=None)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Book {}>'.format(self.id)


# Converts user id from integer into string and routes.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
