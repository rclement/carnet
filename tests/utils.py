import os
import json
import shutil

from flask_testing import TestCase

from carnet import create_app
from carnet.utils.config import absolute_path, get_app_config_path


def test_app_config():
    return {
        'title': 'My Title',
        'subtitle': 'My subtitle',
        'author': 'Me, Myself and I',
        'theme': 'default',
        'pages_path': 'pages',
        'posts_path': 'posts',
        'output_path': 'output',
    }


def create_app_config():
    app_config = test_app_config()
    app_config_path = absolute_path('config.json')
    with open(app_config_path, mode='w', encoding='utf-8') as f:
        json.dump(app_config, f, indent=4)
    return app_config


def delete_app_config():
    app_config_path = absolute_path('config.json')
    if os.path.isfile(app_config_path):
        os.remove(app_config_path)


def create_folders(app_config):
    def _create_folder(path):
        folder = absolute_path(path)
        if path and not os.path.isdir(folder):
            os.mkdir(folder)

    folders = [
        'instance',
        app_config.get('posts_path', None),
        app_config.get('pages_path', None),
        app_config.get('output_path', None)
    ]

    for f in folders:
        _create_folder(f)


def delete_folders(app_config):
    def _delete_folder(path):
        folder = absolute_path(path)
        if path and os.path.isdir(folder):
            shutil.rmtree(folder)

    folders = [
        'instance',
        app_config.get('posts_path', None),
        app_config.get('pages_path', None),
        app_config.get('output_path', None)
    ]

    for f in folders:
        _delete_folder(f)


def create_test_app():
    return create_app(
        config_name='testing'
    )


class TestAppConfigured(TestCase):

    def create_app(self):
        self.app_config = create_app_config()
        create_folders(self.app_config)
        return create_test_app()

    def tearDown(self):
        delete_folders(self.app_config)
        delete_app_config()


class TestAppNotConfigured(TestCase):

    def create_app(self):
        return create_test_app()
