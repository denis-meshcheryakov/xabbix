import os
from flask import Flask


def init_app(test_config=None):
    """Creates flask app"""
    server = Flask('markup_service')
    if test_config:
        server.config.from_object('webapp.config.DevConfig')
    else:
        server.config.from_object('webapp.config.BaseConfig')

    server.template_folder = os.path.abspath(
        r'C:\Users\User\PycharmProjects\xabbix\webapp\templates')

    server.config.from_pyfile(r'webapp\\config.py')

    with server.app_context():
        from webapp import routes

        from webapp.dashapp import init_dash_app

        app = init_dash_app(server)

    return app
