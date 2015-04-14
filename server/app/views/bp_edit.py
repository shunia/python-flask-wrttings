from flask import Blueprint

bp = Blueprint('edit', __name__)

@bp.route('/')
def edit():
    return "Start editing"