import os


class DevConfig:
    DEBUG = True


class BaseConfig:
    DEBUG = False

TEMPLATE_FOLDER = os.path.abspath(r'/mnt/c/Users/User/PycharmProjects/xabbix/webapp/templates')

SECRET_KEY = 'kslknsbloiewboin'
