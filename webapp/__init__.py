import os
from flask import Flask


def init_app(test_config=None):
    """Creates flask app"""
    app = Flask('markup_service')
    if test_config:
        app.config.from_object('webapp.config.DevConfig')
    else:
        app.config.from_object('webapp.config.BaseConfig')

    app.template_folder = os.path.abspath(
        r'C:\Users\User\PycharmProjects\xabbix\webapp\templates')
    # SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = 'kslknsbloiewboin'

    with app.app_context():
        from webapp import routes

        from webapp.dashapp import init_dash_app

        app = init_dash_app(app)

    return app
