from flask import Blueprint

from ..utils.config import absolute_path


def create_assets_blueprint(static_folder):
    return Blueprint(
        'assets',
        __name__,
        static_folder=absolute_path(static_folder)
    )
