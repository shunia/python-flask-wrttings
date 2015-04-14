from flask import Blueprint

bp = Blueprint('login', __name__)

@bp.route('/')
def login():
    return "Login here"