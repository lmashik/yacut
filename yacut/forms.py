from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=(
            DataRequired(message='Обязательное поле'),
            Length(
                1, 256,
                message='Длина ссылки должна быть не более 256 символов'
            ),
            URL(message='Некорректный URL')
        )
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=(
            Length(
                1, 16,
                message='Длина идентификатора должна быть не более 16 символов'
            ),
            Optional()
        )
    )
    submit = SubmitField('Создать')
