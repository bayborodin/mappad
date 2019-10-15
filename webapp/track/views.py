from flask import Blueprint
from flask import render_template
from flask_login import login_required

from webapp.track.forms import AddTrackForm

blueprint = Blueprint('track', __name__, url_prefix='/tracks')


@blueprint.route('/new')
@login_required
def add_track():
    title = 'Добавить GPS трек'
    form = AddTrackForm()
    return render_template('track/addtrack.jinja', page_title=title, form=form)
