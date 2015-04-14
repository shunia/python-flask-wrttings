from flask import Blueprint

bp = Blueprint('profile', __name__)

@bp.route('/')
def profile():
    return "Profile page here"