from flask import Blueprint

from ..utils.data import (get_all_categories, get_categorized_pages,
                          get_categorized_posts, get_global_config)
from ..utils.render import render_template


bp = Blueprint('categories', __name__, url_prefix='/categories')


@bp.route('/')
def categories():
    all_categories = get_all_categories()

    return render_template(
        'categories.html',
        global_config=get_global_config(),
        categories=all_categories
    )


@bp.route('/<string:category_name>/')
def category(category_name):
    categorized_pages = get_categorized_pages(category_name)
    categorized_posts = get_categorized_posts(category_name)

    return render_template(
        'category.html',
        global_config=get_global_config(),
        category=category_name,
        pages=categorized_pages,
        posts=categorized_posts
    )
