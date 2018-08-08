import os
import os.path
import string

from base64 import b64encode
from codecs import open
from flask import Flask, redirect, request, url_for
from flask_flatpages import FlatPages
from flask_moment import Moment
from flask_themes import setup_themes
from flask_htmlmin import HTMLMIN
from flask_frozen import Freezer
from flask_pretty import Prettify

from .__about__ import (__title__, __version__, __description__, __author__,
                        __author_email__, __url__, __license__)

from .config import get_app_config
from .utils.assets import create_assets_blueprint
from .utils.config import (absolute_path, check_app_config_present,
                           load_user_config, update_app_config)
from .utils.render import render_template


pages = FlatPages(name='pages')
posts = FlatPages(name='posts')
moment = Moment()
minify = HTMLMIN()
prettify = Prettify()
freezer = Freezer(with_no_argument_rules=False, log_url_for=True)


# ------------------------------------------------------------------------------

def register_freezer_generators(spa_theme):
    @freezer.register_generator
    def home_url_generator():
        urls = [
            ('home.index', {})
        ]
        return urls

    if not spa_theme:
        @freezer.register_generator
        def pages_url_generator():
            urls = [
                ('pages.pages', {})
            ]
            urls.extend([
                ('pages.page', {'path': p.path}) for p in pages
            ])
            return urls

        @freezer.register_generator
        def post_url_generator():
            urls = [
                ('posts.posts', {})
            ]
            urls.extend([
                ('posts.post', {'path': p.path}) for p in posts
            ])
            return urls

        @freezer.register_generator
        def categories_url_generator():
            from .utils.data import get_all_categories
            all_categories = get_all_categories()

            urls = [
                ('categories.categories', {})
            ]
            urls.extend([
                ('categories.category', {'category_name': c['name']})
                for c in all_categories
            ])
            return urls

        @freezer.register_generator
        def tags_url_generator():
            from .utils.data import get_all_tags
            all_tags = get_all_tags()

            urls = [
                ('tags.tags', {})
            ]
            urls.extend([
                ('tags.tag', {'tag_name': t['name']}) for t in all_tags
            ])
            return urls


# ------------------------------------------------------------------------------


def create_instance_config(instance_config_file):
    if not os.path.isfile(instance_config_file):
        instance_template = string.Template('SECRET_KEY=\'$secret_key\'')
        instance_values = {
            'secret_key': b64encode(os.urandom(32)).decode('utf-8'),
        }
        instance_config_text = instance_template.substitute(instance_values)

        instance_dir = os.path.dirname(instance_config_file)
        if not os.path.isdir(instance_dir):
            os.makedirs(instance_dir)

        with open(instance_config_file, 'w', 'utf-8') as f:
            f.write(instance_config_text)


def create_app(
    config_name='default', user_config_file=None, instance_path=None
):
    app_kwargs = {}
    if instance_path:
        app_kwargs['instance_path'] = absolute_path(instance_path)

    app = Flask(import_name=__name__, **app_kwargs)

    app_config = get_app_config(config_name)
    if user_config_file is not None:
        user_config = load_user_config(user_config_file)
        app_config = update_app_config(app_config, user_config)
    app.config.from_object(app_config)

    instance_config_file = os.path.join(app.instance_path, 'config.py')
    create_instance_config(instance_config_file)
    app.config.from_pyfile(instance_config_file)

    pages.init_app(app)
    posts.init_app(app)
    moment.init_app(app)
    setup_themes(app)
    minify.init_app(app)
    prettify.init_app(app)
    freezer.init_app(app)

    assets_bp = create_assets_blueprint(app_config.ASSETS_ROOT)
    app.register_blueprint(assets_bp)

    from .views.admin import bp as admin_bp
    from .views.archives import bp as archives_bp
    from .views.categories import bp as categories_bp
    from .views.home import bp as home_bp
    from .views.pages import bp as pages_bp
    from .views.posts import bp as posts_bp
    from .views.quickstart import bp as quickstart_bp
    from .views.tags import bp as tags_bp
    app.register_blueprint(admin_bp)
    app.register_blueprint(archives_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(pages_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(quickstart_bp)
    app.register_blueprint(tags_bp)

    app_theme = app.theme_manager.themes.get(app.config.get('THEME'), None)
    register_freezer_generators(app_theme.info.get('spa', False))

    @app.before_request
    def redirect_to_quickstart():
        quickstart_endpoint = 'quickstart.quickstart'
        exclude_quickstart_redirect = ['home.pygments_css']

        if (not check_app_config_present() and
                request.endpoint != quickstart_endpoint and
                request.endpoint not in exclude_quickstart_redirect):
            return redirect(url_for(quickstart_endpoint))

        return None

    @app.errorhandler(404)
    def page_not_found(error):
        from .utils.data import get_global_config
        return render_template(
            '404.html', global_config=get_global_config()
        ), 404

    return app
