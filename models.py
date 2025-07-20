from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    name = db.Column(db.String(100))
    dob = db.Column(db.String(20))
    conditions = db.Column(db.Text)