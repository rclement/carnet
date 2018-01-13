import os
import json
import shutil

from flask_testing import TestCase

from carnet import create_app
from carnet.utils.config import absolute_path


test_user_config_file = 'config.json'


def test_user_config():
    return {
        'title': 'My Title',
        'subtitle': 'My subtitle',
        'author': 'Me, Myself and I',
        'theme': 'default',
        'assets_path': 'assets',
        'pages_path': 'pages',
        'posts_path': 'posts',
        'output_path': 'output',
    }


def create_user_config():
    user_config = test_user_config()
    user_config_path = absolute_path(test_user_config_file)
    with open(user_config_path, mode='w', encoding='utf-8') as f:
        json.dump(user_config, f, indent=4)
    return user_config


def delete_user_config():
    user_config_path = absolute_path('config.json')
    if os.path.isfile(user_config_path):
        os.remove(user_config_path)


def create_folders(user_config):
    def _create_folder(path):
        folder = absolute_path(path)
        if path and not os.path.isdir(folder):
            os.mkdir(folder)

    folders = [
        'instance',
        user_config.get('assets_path', None),
        user_config.get('posts_path', None),
        user_config.get('pages_path', None),
        user_config.get('output_path', None)
    ]

    for f in folders:
        _create_folder(f)


def delete_folders(user_config):
    def _delete_folder(path):
        folder = absolute_path(path)
        if path and os.path.isdir(folder):
            shutil.rmtree(folder)

    folders = [
        'instance',
        user_config.get('assets_path', None),
        user_config.get('posts_path', None),
        user_config.get('pages_path', None),
        user_config.get('output_path', None)
    ]

    for f in folders:
        _delete_folder(f)


def create_test_app():
    return create_app(
        config_name='testing',
        user_config_file=test_user_config_file,
        instance_path='instance'
    )


class TestAppConfigured(TestCase):

    def create_app(self):
        self.user_config = create_user_config()
        create_folders(self.user_config)
        return create_test_app()

    def tearDown(self):
        delete_folders(self.user_config)
        delete_user_config()


class TestAppNotConfigured(TestCase):

    def create_app(self):
        return create_test_app()
