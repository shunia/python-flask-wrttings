from flask import Blueprint

bp = Blueprint('bp_edit', __name__)

@bp.route('/')
def edit():
    return "Start editing"