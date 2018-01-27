import os

from .utils.config import absolute_path


class Config:
    APP_CONFIG_NAME = 'config.json'

    # user config
    TITLE = ''
    SUBTITLE = ''
    AUTHOR = ''
    THEME = ''
    DEFAULT_THEME = 'default'
    POSTS_PER_PAGE = 2
    TEMPLATES_AUTO_RELOAD = True

    CONTENT_PATH = 'content'
    ASSETS_ROOT = absolute_path(os.path.join(CONTENT_PATH, 'assets'))

    FLATPAGES_PAGES_ROOT = absolute_path(os.path.join(CONTENT_PATH, 'pages'))
    FLATPAGES_PAGES_EXTENSION = '.md'
    FLATPAGES_POSTS_ROOT = absolute_path(os.path.join(CONTENT_PATH, 'posts'))
    FLATPAGES_POSTS_EXTENSION = '.md'

    FREEZER_DESTINATION = absolute_path('output')


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    MINIFY_PAGE = True


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


def get_app_config(config='default'):
    configs = {
        'production': ProductionConfig,
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'default': ProductionConfig,
    }

    return configs.get(config)
