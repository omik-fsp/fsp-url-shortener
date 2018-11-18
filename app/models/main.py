from app import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shorten_url = db.Column(db.String(80), unique=True, nullable=False)
    original_url = db.Column(db.String(120), unique=True, nullable=False)
