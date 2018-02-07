import os
import json
import shutil

from codecs import open
from flask_testing import TestCase

from carnet import create_app
from carnet.utils.config import absolute_path


test_user_config_file = 'config.json'
test_user_folders = [
    'instance',
    'content',
    'content/assets',
    'content/posts',
    'content/pages',
    'content/output'
]


def test_user_config():
    return {
        'title': 'My Title',
        'subtitle': 'My subtitle',
        'author': 'Me, Myself and I',
        'theme': 'default',
    }


def create_user_config():
    user_config = test_user_config()
    user_config_path = absolute_path(test_user_config_file)
    with open(user_config_path, 'w', 'utf-8') as f:
        json.dump(user_config, f, indent=4)
    return user_config


def delete_user_config():
    user_config_path = absolute_path('config.json')
    if os.path.isfile(user_config_path):
        os.remove(user_config_path)


def create_user_folders():
    def _create_folder(path):
        folder = absolute_path(path)
        if path and not os.path.isdir(folder):
            os.makedirs(folder)

    for f in test_user_folders:
        _create_folder(f)


def delete_user_folders():
    def _delete_folder(path):
        folder = absolute_path(path)
        if path and os.path.isdir(folder):
            shutil.rmtree(folder)

    for f in test_user_folders:
        _delete_folder(f)


def create_test_app(user_config_file=None):
    return create_app(
        config_name='testing',
        user_config_file=user_config_file,
        instance_path='instance'
    )


class TestAppConfigured(TestCase):

    def create_app(self):
        self.user_config = create_user_config()
        create_user_folders()
        return create_test_app(test_user_config_file)

    def tearDown(self):
        delete_user_folders()
        delete_user_config()


class TestAppNotConfigured(TestCase):

    def create_app(self):
        return create_test_app()

    def tearDown(self):
        delete_user_folders()
