from flask import Blueprint, render_template

from .. import pages
from ..utils.data import get_global_config


bp = Blueprint('categories', __name__, url_prefix='/categories')


@bp.route('/<string:category_name>/')
def category(category_name):
    tagged_pages = [p for p in pages if category_name in p.meta.get('categories', [])]
    return render_template(
        'tags.html',
        global_config=get_global_config(),
        tag=category_name, pages=tagged_pages
    )
