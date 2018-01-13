from flask import Blueprint

from ..utils.data import (get_all_tags, get_global_config, get_tagged_pages,
                          get_tagged_posts)
from ..utils.render import render_template


bp = Blueprint('tags', __name__, url_prefix='/tags')


@bp.route('/')
def tags():
    all_tags = get_all_tags()

    return render_template(
        'tags.html',
        global_config=get_global_config(),
        tags=all_tags
    )


@bp.route('/<string:tag_name>/')
def tag(tag_name):
    tagged_pages = get_tagged_pages(tag_name)
    tagged_posts = get_tagged_posts(tag_name)

    return render_template(
        'tag.html',
        global_config=get_global_config(),
        tag=tag_name,
        pages=tagged_pages,
        posts=tagged_posts
    )
