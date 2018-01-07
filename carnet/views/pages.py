from flask import Blueprint, render_template

from ..utils.data import get_global_config, get_page


bp = Blueprint('pages', __name__, url_prefix='/pages')


@bp.route('/<path:path>/')
def page(path):
    found_page = get_page(path)
    return render_template(
        'page.html',
        global_config=get_global_config(),
        page=found_page
    )
