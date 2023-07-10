from datetime import datetime
import re

from . import db
from settings import ID_PATTERN


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    # def to_dict(self):
    #     return dict(
    #         id=self.id,
    #         url=self.original,
    #         short_link=self.short,
    #     )
    #
    # def from_dict(self, data):
    #     for field in ('original', 'short'):
    #         if field in data:
    #             setattr(self, field, data[field])

    def save(self):
        if not re.match(ID_PATTERN, self.short):
            raise ValueError(
                'В идентификаторе использованы недопустимые символы'
            )
        db.session.add(self)
        db.session.commit()
