class session_helper(object):
    from flask import current_app, g, request
    from .database import conn_db, close_db
    import app

    @babel.localeselector
    def get_locale():
        user = getattr(g, 'user', None)
        if user is not None:
            return user.locale
        return request.accept_languages.best_match(app.config.LANGUAGES.keys())

    @babel.timezoneselector
    def get_timezone():
        user = getattr(g, 'user', None)
        if user is not None:
            return user.timezone
        return app.config.TIME_ZONE[0]

    @current_app.before_request
    def before_req():
        conn_db()

    @current_app.teardown_appcontext
    def after_req(exception):
        close_db()

