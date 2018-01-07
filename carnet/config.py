import os


class Config:
    APP_CONFIG_NAME = 'config.json'

    TITLE = ''
    SUBTITLE = ''
    AUTHOR = ''
    THEME = ''
    POSTS_PER_PAGE = 2
    TEMPLATES_AUTO_RELOAD = True

    FLATPAGES_PAGES_ROOT = 'pages'
    FLATPAGES_PAGES_EXTENSION = '.md'
    FLATPAGES_POSTS_ROOT = 'posts'
    FLATPAGES_POSTS_EXTENSION = '.md'

    FREEZER_DESTINATION = 'build'


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


def app_config():
    env_config = os.getenv('FLASK_CONFIG', 'default')

    configs = {
        'production': ProductionConfig,
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'default': ProductionConfig,
    }

    return configs.get(env_config)
