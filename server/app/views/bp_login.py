from flask import Blueprint, render_template, redirect, request, make_response
from .forms import LoginForm

bp = Blueprint('login', __name__)

@bp.route('/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            return redirect('/edit')
    return render_template('login.html', form=form, page_name='login')