from flask import render_template, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.jinja', title='Главная')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate():
        return redirect(url_for('index'))
    return render_template('login.jinja', title='Авторизация', form=form)


@app.route('/addtrack')
def add_track():
    return render_template('addtrack.jinja')
