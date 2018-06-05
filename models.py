import datetime
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    # -- tablenam
    __tablename__ = 'users'

    # -- fields
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(255)) # -- , unique=True
    password = db.Column(db.String(66))
    create = db.Column(db.DateTime, default=datetime.datetime.now)

    # -- relationship
    comments = db.relationship('Comment')

    # -- init
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.__create_password(password)

    # -- encrypt password
    def __create_password(self, password):
        return generate_password_hash(password)

    # -- verify password
    def verify_password(self, password):
        return check_password_hash(self.password, password)

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    text = db.Column(db.Text())
    create = db.Column(db.DateTime, default=datetime.datetime.now)
