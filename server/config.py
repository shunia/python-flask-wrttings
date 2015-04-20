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
    DATABASE = "sqlite.db"
    SERVER = "127.0.0.1"
    PORT = 5000
    SECRET_KEY = "!87677kjnj%()0&2^91jkd)"

class conf_dev(conf_base):
    DEBUG = True


class conf_prod(conf_base):
    PORT = 8089