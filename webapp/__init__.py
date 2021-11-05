import os
from flask import Flask


def create_app(test_config=None):
    """Creates flask app"""
    app = Flask(__name__)
    if test_config:
        app.config.from_object('webapp.config.DevConfig')
    else:
        app.config.from_object('webapp.config.BaseConfig')

    app.config.from_object('webapp.config.BaseConfig')
    app.config.from_pyfile('config.py')
    app.template_folder = app.config['TEMPLATE_FOLDER']

    with app.app_context():
        from webapp import routes

        from webapp.dashapp import init_dash_app

        app = init_dash_app(app)

    return app
