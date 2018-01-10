from flask import Blueprint
from flask_flatpages.utils import pygments_style_defs

from ..utils.data import get_latest_posts, get_global_config
from ..utils.render import render_template

bp = Blueprint('home', __name__, url_prefix='')


@bp.route('/')
def latest_posts():
    paged_posts, post_page, post_page_max = get_latest_posts()

    return render_template(
        'latest_posts.html',
        global_config=get_global_config(),
        posts=paged_posts,
        post_page=post_page,
        post_page_max=post_page_max
    )


@bp.route('/<int:offset>/')
def latest_posts_offset(offset):
    paged_posts, post_page, post_page_max = get_latest_posts(offset)

    return render_template(
        'latest_posts_offset.html',
        global_config=get_global_config(),
        posts=paged_posts,
        post_page=post_page,
        post_page_max=post_page_max
    )


@bp.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}
