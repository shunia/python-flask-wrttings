from flask import Blueprint, render_template
from app.helper import *

bp = Blueprint('bp_editor', __name__)

@bp.route('/')
def editor():
    user = current_user_data()

    return render_template('editor.html', page_name='editor', user=user)
