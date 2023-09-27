from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config.from_envvar('FLASK_ENV', silent=True)

from blog.main.routes import main

app.register_blueprint(main)