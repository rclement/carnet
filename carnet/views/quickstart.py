from flask import Blueprint, current_app, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

from ..utils.config import (absolute_path, create_app_folders,
                            get_app_config_path, save_app_config)
from ..utils.render import render_template


bp = Blueprint('quickstart', __name__, url_prefix='/quickstart')


class QuickstartForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle')
    author = StringField('Author', validators=[DataRequired()])
    pages_path = StringField('Pages path', default='pages', validators=[DataRequired()])
    posts_path = StringField('Posts path', default='posts', validators=[DataRequired()])
    output_path = StringField('Output path', default='output', validators=[DataRequired()])
    go = SubmitField('Go')


@bp.route('/', methods=['GET', 'POST'])
def quickstart():
    form = QuickstartForm()
    if form.validate_on_submit():
        current_app.config.update({
            'TITLE': form.title.data,
            'SUBTITLE': form.subtitle.data,
            'AUTHOR': form.author.data,
            'THEME': current_app.config.get('DEFAULT_THEME'),
            'FLATPAGES_PAGES_ROOT': absolute_path(form.pages_path.data),
            'FLATPAGES_POSTS_ROOT': absolute_path(form.posts_path.data),
            'FREEZER_DESTINATION': absolute_path(form.output_path.data),
        })

        save_app_config()
        create_app_folders()

        flash('Configuration file created in \'' + get_app_config_path() + '\'')
        return redirect(url_for('home.latest_posts'))

    return render_template('quickstart.html', title='Quickstart', form=form)
