import random
import string

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap

DEFAULT_ID_LENGTH = 6


def get_unique_short_id():
    char_set = string.ascii_lowercase + string.ascii_lowercase + string.digits
    short_id = ''.join(random.choices(char_set, k=DEFAULT_ID_LENGTH))
    return short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if short is '':
            short = get_unique_short_id()

        url_map = URLMap(
            original=form.original_link.data,
            short=short
        )

        if URLMap.query.filter_by(short=short).first():
            flash(f'Имя {short} уже занято!')
            return render_template('index.html', form=form)

        db.session.add(url_map)
        db.session.commit()
        return render_template('index.html', short=url_map.short, form=form)
    return render_template('index.html', form=form)


@app.route('/<short>')
def forwarding_view(short):
    url_map_obj = URLMap.query.filter_by(short=short).first()
    if url_map_obj is None:
        abort(404)
    original_link = url_map_obj.original
    return redirect(original_link)
