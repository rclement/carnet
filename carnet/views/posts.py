from flask import Blueprint

from ..utils.data import get_all_posts, get_global_config, get_post
from ..utils.render import render_template


bp = Blueprint('posts', __name__, url_prefix='/posts')


@bp.route('/')
def posts():
    all_posts = get_all_posts()

    return render_template(
        'posts.html',
        global_config=get_global_config(),
        posts=all_posts
    )


@bp.route('/<path:path>/')
def post(path):
    found_post = get_post(path)

    return render_template(
        'post.html',
        global_config=get_global_config(),
        post=found_post
    )
