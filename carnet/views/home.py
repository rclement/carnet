from flask import Blueprint
from flask_flatpages.utils import pygments_style_defs

from ..utils.data import get_latest_posts, get_global_config
from ..utils.render import render_template

bp = Blueprint('home', __name__, url_prefix='')


@bp.route('/')
@bp.route('/<int:offset>/')
def index(offset=None):
    paged_posts, post_page, post_page_max = get_latest_posts(offset)

    return render_template(
        'index.html',
        global_config=get_global_config(),
        posts=paged_posts,
        post_page=post_page,
        post_page_max=post_page_max
    )


@bp.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}
