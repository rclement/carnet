from flask import Blueprint, current_app, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

from flask_themes import get_themes_list

from ..utils.config import (create_app_folders, get_app_config_path,
                            save_app_config)
from ..utils.render import render_template


bp = Blueprint('quickstart', __name__, url_prefix='/quickstart')


class QuickstartForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle')
    author = StringField('Author', validators=[DataRequired()])
    theme = SelectField('Theme', default='default')
    go = SubmitField('Go')


@bp.route('/', methods=['GET', 'POST'])
def quickstart():
    form = QuickstartForm()
    form.theme.choices = [(t.identifier, t.name) for t in get_themes_list()]

    if form.validate_on_submit():
        current_app.config.update({
            'TITLE': form.title.data,
            'SUBTITLE': form.subtitle.data,
            'AUTHOR': form.author.data,
            'THEME': form.theme.data,
        })

        save_app_config()
        create_app_folders()

        flash(
            'Configuration file created in \'' + get_app_config_path() + '\''
        )
        return redirect(url_for('home.index'))

    form.title.data = current_app.config.get('TITLE')
    form.subtitle.data = current_app.config.get('SUBTITLE')
    form.author.data = current_app.config.get('AUTHOR')
    form.title.data = current_app.config.get('TITLE')
    form.theme.data = current_app.config.get('THEME')
    return render_template('quickstart.html', title='Quickstart', form=form)
