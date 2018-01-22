from flask_script import Manager

from . import create_app, freezer


def create_app_config(config_name='default'):
    return create_app(
        config_name=config_name,
        instance_path='instance',
        user_config_file='config.json'
    )


# ------------------------------------------------------------------------------


def freeze():
    freezer.freeze()


def check():
    freezer.run(debug=True)


# ------------------------------------------------------------------------------


def main():
    manager = Manager(create_app_config)
    manager.command(freeze)
    manager.command(check)
    manager.run()


# ------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
