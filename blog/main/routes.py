import os
import sys

from flask import current_app, request, render_template, Blueprint



main = Blueprint('main', __name__)


@main.route('/')
def home():
    flask_ins = current_app
    server_info = {
        'Server Host': request.host,
        'Server URL Root': request.url_root,
        'Environment': current_app.config.get('ENV'),
        'server_software': os.environ.get('SERVER_SOFTWARE'),
        'port': current_app.config.get('PORT'),
        'root_path': current_app.config.get('root_path'),
        'DEBUG': current_app.config.get('DEBUG'),
        'TESTING': current_app.config.get('TESTING'),
        'WERKZEUG_RUN_MAIN': os.environ.get('WERKZEUG_RUN_MAIN'),
        'ROUTS': current_app.url_map,
        'wsgi - SERVER_SOFTWARE ': request.environ['SERVER_SOFTWARE'],
        'wsgi - multithread ': request.environ['wsgi.multithread'],
        'wsgi - multiprocess ': request.environ['wsgi.multiprocess'],
        'wsgi - REMOTE_ADDR': request.environ['REMOTE_ADDR'],
        'wsgi - REMOTE_PORT': request.environ['REMOTE_PORT'],
        'wsgi - SERVER_NAME': request.environ['SERVER_NAME'],
        'wsgi - SERVER_PORT': request.environ['SERVER_PORT'],
        'wsgi - HTTP_HOST': request.environ['HTTP_HOST'],
        'base_dir': os.path.abspath(os.path.dirname(__file__)),
        'FLASK_ENV': current_app.config.from_envvar('FLASK_ENV', silent=True),
        'FLASK_CONFIG': os.getenv('FLASK_CONFIG') or 'default',

    }
    return render_template('main/home.html', current_app=flask_ins, server_info=server_info)


@main.route('/settings')
def get_settings():
    # Получаем все настройки Flask из объекта конфигурации
    settings = {}
    for key, value in current_app.config.items():
        settings[key] = value

    # Выводим настройки в формате JSON
    return render_template('main/env_viriables.html', env_variables=settings)


@main.route('/env')
def list_environment_variables():
    env_variables = os.environ
    return render_template('main/env_viriables.html', env_variables=env_variables)


@main.route('/gunicorn')
def show_gunicorn_conf():
    conf_contents = "File gunicorn.conf.py not found."
    conf_contents2 = sys.argv
    settings_dict = os.environ.get('c.')
    try:
        with open('/opt/startup/gunicorn.conf.py', 'r') as conf_file:
            conf_contents = conf_file.read()
        return render_template('main/gunicorn_conf.html', conf_contents=conf_contents, conf_contents2=conf_contents2,
                               settings_dict=settings_dict)
    except FileNotFoundError:
        return render_template('main/gunicorn_conf.html', conf_contents="File gunicorn.conf.py not found.",
                               conf_contents2=conf_contents2, settings_dict=settings_dict)
