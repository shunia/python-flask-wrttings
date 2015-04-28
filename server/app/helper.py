from app import app, babel

@babel.localeselector
def get_locale():
    from flask import g, request
    from app import app

    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    print app.config
    return request.accept_languages.best_match(app.config["LANGUAGES"].keys())

@babel.timezoneselector
def get_timezone():
    from flask import g
    from app import app

    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone
    return app.config.TIME_ZONE[0]

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

def current_user(uid=None):
    from flask import session

    if uid is not None and uid >= 0:
        session['user_credential'] = uid
    elif 'user_credential' in session:
        return session['user_credential'];
    
    return None
