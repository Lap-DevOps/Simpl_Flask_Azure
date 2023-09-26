import os

from flask import Flask, render_template, current_app, request, jsonify

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config.from_envvar('FLASK_ENV', silent=True)


@app.route('/')
def home():
    flask_ins = current_app
    server_info = {
        'Server Host': request.host,
        'Server URL Root': request.url_root,
        'Environment': app.config.get('ENV'),
        'server_software': os.environ.get('SERVER_SOFTWARE'),
        'port': app.config.get('PORT'),
        'root_path': app.config.get('root_path'),
        'DEBUG': app.config.get('DEBUG'),
        'TESTING': app.config.get('TESTING'),
        'WERKZEUG_RUN_MAIN': os.environ.get('WERKZEUG_RUN_MAIN'),
        'ROUTS': app.url_map,
        'wsgi - SERVER_SOFTWARE ': request.environ['SERVER_SOFTWARE'],
        'wsgi - multithread ': request.environ['wsgi.multithread'],
        'wsgi - multiprocess ': request.environ['wsgi.multiprocess'],
        'wsgi - REMOTE_ADDR': request.environ['REMOTE_ADDR'],
        'wsgi - REMOTE_PORT': request.environ['REMOTE_PORT'],
        'wsgi - SERVER_NAME': request.environ['SERVER_NAME'],
        'wsgi - SERVER_PORT': request.environ['SERVER_PORT'],
        'wsgi - HTTP_HOST': request.environ['HTTP_HOST'],

    }
    return render_template('home.html', current_app=flask_ins, server_info=server_info)


@app.route('/settings')
def get_settings():
    # Получаем все настройки Flask из объекта конфигурации
    settings = {}
    for key, value in app.config.items():
        settings[key] = value

    # Выводим настройки в формате JSON
    return render_template('env_viriables.html', env_variables=settings)


@app.route('/env')
def list_environment_variables():
    env_variables = os.environ
    return render_template('env_viriables.html', env_variables=env_variables)


if __name__ == '__main__':
    app.run()
