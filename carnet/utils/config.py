import os
import json

from codecs import open
from flask import current_app


def absolute_path(rel_path):
    return os.path.abspath(rel_path or '')


def relative_path(abs_path):
    return os.path.relpath(abs_path or '')


def get_app_config_path():
    app_config_name = current_app.config.get('APP_CONFIG_NAME', '')
    return absolute_path(app_config_name)


def check_app_config_present():
    app_config_path = get_app_config_path()
    return os.path.isfile(app_config_path)


def load_user_config(user_config_file):
    app_config = {}

    app_config_path = absolute_path(user_config_file)
    if os.path.isfile(app_config_path):
        with open(app_config_path, mode='r', encoding='utf-8') as f:
            app_config = json.load(f)

    return app_config


def update_app_config(app_config, user_config):
    default_theme = app_config.DEFAULT_THEME
    user_theme = user_config.get('theme', None)
    if not user_theme:
        user_theme = default_theme

    app_config.TITLE = user_config.get('title', '')
    app_config.SUBTITLE = user_config.get('subtitle', '')
    app_config.AUTHOR = user_config.get('author', '')
    app_config.THEME = user_theme
    app_config.ASSETS_ROOT = absolute_path(user_config.get('assets_path'))
    app_config.FLATPAGES_PAGES_ROOT = absolute_path(user_config.get('pages_path'))
    app_config.FLATPAGES_POSTS_ROOT = absolute_path(user_config.get('posts_path'))
    app_config.FREEZER_DESTINATION = absolute_path(user_config.get('output_path'))

    return app_config


def save_app_config():
    default_theme = current_app.config.get('DEFAULT_THEME')
    app_config = {
        'title': current_app.config.get('TITLE', ''),
        'subtitle': current_app.config.get('SUBTITLE'),
        'author': current_app.config.get('AUTHOR', ''),
        'theme': current_app.config.get('THEME', default_theme),
        'assets_path': relative_path(current_app.config.get('ASSETS_ROOT', '')),
        'pages_path': relative_path(current_app.config.get('FLATPAGES_PAGES_ROOT', '')),
        'posts_path': relative_path(current_app.config.get('FLATPAGES_POSTS_ROOT', '')),
        'output_path': relative_path(current_app.config.get('FREEZER_DESTINATION', '')),
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
