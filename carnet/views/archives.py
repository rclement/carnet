from datetime import date

from flask import Blueprint

from ..utils.data import (get_archives, get_global_config, get_monthly_posts,
                          get_yearly_posts)
from ..utils.render import render_template


bp = Blueprint('archives', __name__, url_prefix='/archives')


@bp.route('/')
def archives():
    all_archives = get_archives()

    return render_template(
        'archives.html',
        global_config=get_global_config(),
        archives=all_archives
    )


@bp.route('/<int:year>/')
def yearly(year):
    yearly_posts = get_yearly_posts(year)

    return render_template(
        'archives_yearly.html',
        global_config=get_global_config(),
        archive_date=date(year=year, month=1, day=1),
        posts=yearly_posts
    )


@bp.route('/<int:year>/<int:month>/')
def monthly(year, month):
    monthly_posts = get_monthly_posts(year, month)

    return render_template(
        'archives_monthly.html',
        global_config=get_global_config(),
        archive_date=date(year=year, month=month, day=1),
        posts=monthly_posts
    )
