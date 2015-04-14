from flask import Blueprint, render_template

bp = Blueprint('index', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    from app import app
    return render_template('index.html')