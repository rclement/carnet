import os
import json

from carnet.utils.config import get_app_config_path


def test_app_config():
    return {
        'title': 'My Title',
        'subtitle': 'My subtitle',
        'author': 'Me, Myself and I',
        'theme': '',
        'pages_path': 'pages',
        'posts_path': 'posts',
        'output_path': 'output',
    }


def create_app_config():
    app_config_path = get_app_config_path()
    with open(app_config_path, mode='w', encoding='utf-8') as f:
        json.dump(test_app_config(), f, indent=4)


def delete_app_config():
    app_config_path = get_app_config_path()
    if os.path.isfile(app_config_path):
        os.remove(app_config_path)
