import os
import os.path

from flask_script import Manager, prompt
from flask_frozen import Freezer

from . import create_app, pages, posts
from .utils.config import save_app_config


def absolute_path(relative_path):
    return os.path.abspath(relative_path or '')


user_instance_path = 'instance'
user_config_file = 'config.json'
app = create_app(
    instance_path=user_instance_path,
    user_config_file=user_config_file
)
manager = Manager(app)
freezer = Freezer(app)


# ------------------------------------------------------------------------------


@manager.command
def quickstart():
    title = prompt('title', default='')
    subtitle = prompt('subtitle', default='')
    author = prompt('author', default='')
    theme = prompt('theme', default='default')

    pages_path = prompt('pages_path', default='pages')
    if not pages_path:
        print('A valid path for the pages is required.')
        return

    posts_path = prompt('posts_path', default='posts')
    if not posts_path:
        print('A valid path for the posts is required.')
        return

    output_path = prompt('output_path', default='output')
    if not output_path:
        print('A valid path for the output is required.')
        return

    with manager.app.app_context():
        app.config.update({
            'TITLE': title,
            'SUBTITLE': subtitle,
            'AUTHOR': author,
            'THEME': theme,
            'FLATPAGES_PAGES_ROOT': pages_path,
            'FLATPAGES_POSTS_ROOT': posts_path,
            'FREEZER_DESTINATION': output_path,
        })
        save_app_config()


# ------------------------------------------------------------------------------


@freezer.register_generator
def page_url_generator():
    return [
        ('pages.page', {'path': p.path}) for p in pages
    ]


@freezer.register_generator
def post_url_generator():
    return [
        ('posts.post', {'path': p.path}) for p in posts
    ]


@manager.command
def freeze():
    freezer.freeze()


@manager.command
def check():
    freezer.run(debug=True)


# ------------------------------------------------------------------------------


def main():
    manager.run()


if __name__ == '__main__':
    main()
