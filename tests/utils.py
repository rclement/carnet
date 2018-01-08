import os
import json
import shutil

from carnet import create_app
from carnet.utils.config import absolute_path, get_app_config_path


def cleanup_folders():
    def _delete_folder(path):
        folder = absolute_path(path)
        if os.path.isdir(folder):
            shutil.rmtree(folder)

    folders = [
        'instance', 'pages', 'posts', 'output'
    ]

    for f in folders:
        _delete_folder(f)


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


def create_test_app():
    cleanup_folders()
    return create_app(
        config_name='testing'
    )
