from flask import Blueprint, render_template

from .. import pages
from ..utils.data import get_global_config


bp = Blueprint('tags', __name__, url_prefix='/tags')


@bp.route('/<string:tag_name>/')
def tag(tag_name):
    tagged_pages = [p for p in pages if tag_name in p.meta.get('tags', [])]
    return render_template(
        'tags.html',
        global_config=get_global_config(),
        tag=tag_name,
        pages=tagged_pages
    )
