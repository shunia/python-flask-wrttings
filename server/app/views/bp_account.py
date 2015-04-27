from flask import (Blueprint, render_template, redirect, 
                    request, make_response, g, url_for)
from .forms import LoginForm
import app.helper
from ..models.model import User

bp = Blueprint('bp_account', __name__)

@bp.route('/')
def index():
    user = user_logged_in()
    if user is not None:
        return redirect(url_for('/profile', user=user))
    else:
        return redirect(url_for('/login'))

@bp.route('/login', methods=('GET', 'POST'))
def login():
    error = None
    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():
        error = user_login_validate(form.email.data, form.password.data)
        if error is None:
            return redirect(url_for('bp_edit.edit'))
    return render_template('login.html', form=form, page_name='login', error=error)

def user_login_validate(email, password):
    user = User.query.filter_by(email=email).first()
    if user is None or not user.check_password(password):
        return "Wrong password or email address"
    return None

@bp.route('/register', methods=('GET', 'POST'))
def register():
    return "Register here"

@bp.route('/profile', methods=('GET', 'POST'))
def profile(user):
    if request.method == "GET":
        if user is not None:

    return "Profile here"