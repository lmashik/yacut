from datetime import datetime

from yacut import db


class URLMap(db.Model):
    id = db.Colomn(db.Integer, primary_key=True)
    original = db.Colomn(db.String(256), nullable=False)
    short = db.Colomn(db.String(6), nullable=False)
    timestamp = db.Colomn(db.DateTime, index=True, default=datetime.utcnow)
