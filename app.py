import os
import sys

from flask import Flask, render_template, current_app, request

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
        'base_dir': os.path.abspath(os.path.dirname(__file__)),

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


@app.route('/gunicorn')
def show_gunicorn_conf():
    conf_contents = "File gunicorn.conf.py not found."
    conf_contents2 = sys.argv
    settings_dict = vars(c)
    try:
        with open('/opt/startup/gunicorn.conf.py', 'r') as conf_file:
            conf_contents = conf_file.read()
        return render_template('gunicorn_conf.html', conf_contents=conf_contents, conf_contents2=conf_contents2,
                               settings_dict=settings_dict)
    except FileNotFoundError:
        return render_template('gunicorn_conf.html', conf_contents="File gunicorn.conf.py not found.",
                               conf_contents2=conf_contents2)


if __name__ == '__main__':
    app.run()
