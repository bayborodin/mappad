from flask import render_template
from flask_login import login_required
from app import app, db
from app.forms import AddTrackForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.jinja', title='Главная')


@app.route('/addtrack')
@login_required
def add_track():
    title = 'Добавить GPS трек'
    form = AddTrackForm()
    return render_template('addtrack.jinja', page_title=title, form=form)
