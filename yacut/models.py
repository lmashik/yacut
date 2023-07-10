import re
from datetime import datetime

from settings import ID_PATTERN
from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def save(self):
        if not re.match(ID_PATTERN, self.short):
            raise ValueError(
                'В идентификаторе использованы недопустимые символы'
            )
        db.session.add(self)
        db.session.commit()
