from http import HTTPStatus

from flask import abort, flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        original = form.original_link.data
        short = form.custom_id.data

        if URLMap.query.filter_by(short=short).first():
            flash(f'Имя {short} уже занято!')
            return render_template('index.html', form=form)

        if not short:
            short = get_unique_short_id()

        url_map_obj = URLMap(
            original=original,
            short=short
        )

        db.session.add(url_map_obj)
        db.session.commit()
        return render_template('index.html', short=short, form=form)
    return render_template('index.html', form=form)


@app.get('/<short>')
def forwarding_view(short):
    url_map_obj = URLMap.query.filter_by(short=short).first()
    if url_map_obj is None:
        abort(HTTPStatus.NOT_FOUND)
    original_link = url_map_obj.original
    return redirect(original_link)
