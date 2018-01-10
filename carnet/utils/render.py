from flask import current_app
from flask_themes import render_theme_template


def render_template(template_name, **context):
    current_theme = current_app.config.get('THEME')

    return render_theme_template(
        current_theme,
        template_name,
        **context
    )
