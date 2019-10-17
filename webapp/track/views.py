from flask import Blueprint
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from webapp import db
from webapp.track.forms import AddTrackForm
from webapp.track.models import Track

blueprint = Blueprint('track', __name__, url_prefix='/tracks')


@blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def add_track():
    title = 'Добавить GPS трек'
    form = AddTrackForm()
    if form.validate_on_submit():
        track = Track(
            title=form.title.data,
            author=current_user,
            description=form.description.data,
            raw_gpx=form.rawgpx.data
        )
        db.session.add(track)
        db.session.commit()
        flash('GPX трек сохранен.')
        return redirect(url_for('track.my_tracks'))
    return render_template('track/addtrack.jinja', page_title=title, form=form)


@blueprint.route('/my')
@login_required
def my_tracks():
    title = 'Мои GPS треки'
    tracks = current_user.tracks.all()
    return render_template('track/my_tracks.jinja', page_title=title, tracks=tracks)
