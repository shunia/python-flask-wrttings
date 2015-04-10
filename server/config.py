class config(object):
    def get_config(self, type):
        conf_name = type + "_conf"
        return getattr(self, conf_name)()

    def dev_conf():
        return dev_conf

    def prod_conf():
        return prod_conf

    class base_conf(object):
        DEBUG = False
        TESTING = False
        DATABASE = "sqlite.db"
        SERVER = "127.0.0.1"
        PORT = "5000"

    class dev_conf(base_conf):
        DEBUG = True

    class prod_conf(base_conf):
        PORT = "8089"