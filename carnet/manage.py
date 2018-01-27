from flask_script import Manager

from . import create_app, freezer


def create_app_config(dev=False):
    return create_app(
        config_name='development' if dev else 'default',
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
    manager.add_option(
        '-d', '--dev', action='store_true', dest='dev', required=False,
        help='Create the app in development mode (enable debugging)'
    )
    manager.command(freeze)
    manager.command(check)
    manager.run()


# ------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
