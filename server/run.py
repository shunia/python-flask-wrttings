#!venv/bin/python

def init(env):
    from app import set_config, run
    from config import config as __config_generator__

    """init config generator"""
    conf_gen = __config_generator__()
    """get current detailed config of this app"""
    conf = conf_gen.get_config(type=env)
    """if it exists,set config to trigger initialization of 
       flask app and everything else"""
    if conf:
        set_config(conf)
    return conf

def startup():
    from app import app
    
    app.run(app.config["HOST"], app.config["PORT"])

import sys
"""run"""
if __name__ == "__main__":
    if len(sys.argv) == 1:
            init("dev")
            startup()
    else:
        for arg in sys.argv:
            if arg.startswith('env='):
                init(arg[4:])
            if arg == "run":
                startup()
            elif arg == "createdb":
                from app import db
                from app.models import model

                db.create_all()
            elif arg == "dropdb":
                from app import db

                db.drop_all()