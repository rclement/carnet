import os
import json

from codecs import open
from flask import current_app


def absolute_path(relative_path):
    return os.path.abspath(relative_path or '')


def get_app_config_path():
    app_config_name = current_app.config.get('APP_CONFIG_NAME', '')
    return absolute_path(app_config_name)


def check_app_config_present():
    app_config_path = get_app_config_path()
    return os.path.isfile(app_config_path)


def load_app_config():
    app_config_path = get_app_config_path()
    if not check_app_config_present():
        return {}

    with open(app_config_path, mode='r', encoding='utf-8') as f:
        app_config = json.load(f)

    current_app.config.update({
        'TITLE': app_config.get('title', ''),
        'SUBTITLE': app_config.get('subtitle', ''),
        'AUTHOR': app_config.get('author', ''),
        'THEME': app_config.get('theme', ''),
        'FLATPAGES_PAGES_ROOT': absolute_path(app_config.get('pages_path')),
        'FLATPAGES_POSTS_ROOT': absolute_path(app_config.get('posts_path')),
        'FREEZER_DESTINATION': absolute_path(app_config.get('output_path')),
    })


def save_app_config():
    app_config = {
        'title': current_app.config.get('TITLE', ''),
        'subtitle': current_app.config.get('SUBTITLE'),
        'author': current_app.config.get('AUTHOR', ''),
        'theme': current_app.config.get('THEME', None),
        'pages_path': current_app.config.get('FLATPAGES_PAGES_ROOT', ''),
        'posts_path': current_app.config.get('FLATPAGES_POSTS_ROOT', ''),
        'output_path': current_app.config.get('FREEZER_DESTINATION', ''),
    }

    app_config_path = get_app_config_path()
    with open(app_config_path, mode='w', encoding='utf-8') as f:
        json.dump(app_config, f, indent=4)


def create_app_folders():
    directories = [
        current_app.config.get('FLATPAGES_PAGES_ROOT', None),
        current_app.config.get('FLATPAGES_POSTS_ROOT', None),
        current_app.config.get('FREEZER_DESTINATION', None)
    ]

    for d in directories:
        if d and not os.path.isdir(d):
            os.makedirs(d)
