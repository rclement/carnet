from flask import Blueprint

from ..utils.data import get_global_config
from ..utils.render import render_template


bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/', defaults={'path': ''})
@bp.route('/<path:path>')
def admin(path):
    return render_template(
        'admin.html',
        global_config=get_global_config(),
        title='Dashboard'
    )
