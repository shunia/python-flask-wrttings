# coding=utf8
from flask import (Blueprint, render_template, redirect,
                    request, make_response, g, url_for)
from app import db
from ..models.model import User
from ..helper import *                                      # import all functions
from .forms import *

bp = Blueprint('bp_account', __name__)

@bp.route('/')
def index():
    if current_user() is not None:
        return redirect(url_for('bp_account.profile'))
    else:
        return redirect(url_for('bp_account.login'))

@bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    error = None

    if request.method == 'POST':
        print 'registing'
        if form.validate_on_submit():
            error = user_register_validate(form.email.data, form.nickname.data)
            if error is None:
                user = User(form.nickname.data, form.email.data, form.password.data, User.ROLE_REGISTERD)
                db.session.add(user)
                db.session.commit()
                current_user(user.id)                       # save user id into session
                return redirect(url_for('bp_account.profile'))
    return render_template('register.html', form=form, page_name='register', error=error)

def user_register_validate(email, nickname):
    user = User.query.filter_by(email=email).first()
    if user is not None:
        return u'邮件地址已经被使用'
    user = User.query.filter_by(nickname=nickname).first()
    if user is not None:
        return u'昵称已经被使用'
    return None

@bp.route('/login', methods=('GET', 'POST'))
def login():
    error = None
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            error, user = user_login_validate(form.email.data, form.password.data)
            if error is None and user is not None:
                current_user(user.id)                       # save user id into session
                return redirect(url_for('bp_edit.edit'))
    return render_template('login.html', form=form, page_name='login', error=error)

def user_login_validate(email, password):
    error = None
    user = User.query.filter_by(email=email).first()
    if user is None or not user.check_password(password):
        error = u'错误的用户名或密码'
    return error, user

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
    return render_template('profile.html', form=form, page_name='profile', user=user)       # render
