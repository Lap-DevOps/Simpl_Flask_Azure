import os

from flask import Flask

from config import config


def create_app():
    app = Flask(__name__)
    config_name= os.getenv('FLASK_CONFIG') or 'default'
    app.config.from_object(config[config_name])

    from blog.main.routes import main


    app.register_blueprint(main)

    return app
