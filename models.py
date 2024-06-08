import datetime
from flask_sqlalchemy import SQLAlchemy
import pytz

db = SQLAlchemy()

def gmt_plus_4():
    tz = pytz.timezone('Etc/GMT-4')
    return datetime.now(tz)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(1024), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    ROLES = ['intern', 'manager', 'CEO']  # Available roles

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('projects', lazy=True))

    def __repr__(self):
        return f'<Project {self.title}>'
    
class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=gmt_plus_4)
