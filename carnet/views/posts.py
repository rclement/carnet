from flask import Blueprint, render_template

from ..utils.data import get_global_config, get_post


bp = Blueprint('posts', __name__, url_prefix='/posts')


@bp.route('/<path:path>/')
def post(path):
    found_post = get_post(path)
    return render_template(
        'post.html',
        global_config=get_global_config(),
        post=found_post
    )
