from app import app
from app.models.model import User

def current_user(uid=None):
    from flask import session

    if uid is not None and uid >= 0:
        session['user_credential'] = uid
    elif 'user_credential' in session:
        return session['user_credential'];

    return None

def current_user_data():
    uid = current_user()

    if uid is not None:
        return User.query.filter_by(id=uid).first_or_404()

    return None

def sign_out(uid):
    from flask import session

    if uid is not None and \
        uid >= 0 and \
        'user_credential' in session and \
        session['user_credential'] == uid:
        session.pop('user_credential', None);
        return True;

    return False

'''decorators'''
@app.errorhandler(404)
def page_not_found(error):
    return "Page not found!", 404

@app.errorhandler(500)
def internal_server_error(error):
    return "Internal server error!", 500

@app.before_request
def before_req():
    pass

@app.teardown_appcontext
def after_req(exception):
    from flask import g

    db = getattr(g, '_database', None)
    if db is not None:
        if exception is not None:
            db.roll_back()
        else:
            db.session.commit()
