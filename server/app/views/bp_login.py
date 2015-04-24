from flask import (Blueprint, render_template, redirect, 
                    request, make_response, g)
from .forms import LoginForm
from ..helper import session_helper
from ..models.model import User

bp = Blueprint('login', __name__)
helper = session_helper()

@bp.route('/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        return redirect(url_for('edit'))
    return render_template('login.html', form=form, page_name='login')