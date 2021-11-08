import os

class DevConfig:
    DEBUG = True


class BaseConfig:
    DEBUG = False

TEMPLATE_FOLDER = os.path.abspath(r'/home/denis/learn_python/xabbix/webapp/templates')

SECRET_KEY = 'kslknsbloiewboin'
