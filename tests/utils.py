import os

from carnet.utils.config import get_app_config_path


def delete_app_config():
    app_config_path = get_app_config_path()
    if os.path.isfile(app_config_path):
        os.remove(app_config_path)
