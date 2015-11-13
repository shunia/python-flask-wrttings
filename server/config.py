class config(object):
    def get_config(self, type):
        conf_name = type + "_conf"
        conf_func = getattr(self, conf_name)
        if callable(conf_func):
            return conf_func()
        else:
            return None

    def dev_conf(self):
        return conf_dev

    def prod_conf(self):
        return conf_prod

class conf_base(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite.db"
    HOST = "127.0.0.1"
    PORT = 5000
    SECRET_KEY = "!87677kjnj%()0&2^91jkd)"
    TIME_ZONE = ['UTC']
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class conf_dev(conf_base):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///writtings_dev.db"

class conf_prod(conf_base):
    PORT = 8089
    SQLALCHEMY_DATABASE_URI = "mysql://root:7758258hqf@54.65.50.8/writtings"
