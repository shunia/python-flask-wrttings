#!venv/bin/python
from app import set_config, app
from config import config as __config_generator__

"""set enviroment here manually"""
ENV = "dev"
"""init config generator"""
conf_gen = __config_generator__()
"""get current detailed config of this app"""
conf = conf_gen.get_config(type=ENV)
"""if it exists,set config to trigger initialization of 
   flask app and everything else"""
if conf:
    set_config(conf)

"""run"""
if __name__ == "__main__":
    if conf:
        app.run(server=conf["SERVER"], port=conf["PORT"])