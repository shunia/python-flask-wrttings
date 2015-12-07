# coding=utf8
from flask import (Blueprint, render_template, redirect,
                    request, make_response, g, url_for)
from app import db
from ..models.model import User
from ..helper import *                                      # import all functions
from .forms import *

bp = Blueprint('bp_user', __name__)

@bp.route('/')
def home(): 
    user = current_user_data()
    
    return render_template('user.html', page_name='user', user=user)

@bp.route('/profile', methods=('GET', 'POST'))
def profile():
    form = ProfileForm()
    user = None
    uid = current_user()

    if request.method == 'GET':
        if uid is not None:
            user = User.query.filter_by(id=uid).first_or_404()
        else:
            return redirect(url_for('bp_account.login'))
    else:
        ''' editing '''
        uid = form.id.data
        if uid is not None and form.validate_on_submit():   # basic validation
            user = User.query.filter_by(id=uid).first()     # find user
            if user is not None:                            # start update
                user.nickname = form.nickname.data
                user.age = form.age.data
                user.email = form.email.data
                db.session.commit()
                flush(u'资料已保存!')               # updated and message flushed
    return render_template('user_profile.html', form=form, page_name='profile', user=user)       # render