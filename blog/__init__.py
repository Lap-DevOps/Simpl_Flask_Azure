from flask import Flask

from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from blog.main.routes import main
    app.config.from_envvar('FLASK_ENV', silent=True)

    app.register_blueprint(main)

    return app
