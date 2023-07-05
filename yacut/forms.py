from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length


class OpinionForm(FlaskForm):
    original_link = URLField(
        'Введите полную ссылку',
        validators=(
            DataRequired(message='Обязательное поле'),
            Length(1, 256),
        )
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=(
            DataRequired(message='Обязательное поле'),
            Length(6, 6)
        )
    )
    submit = SubmitField('Создать')
