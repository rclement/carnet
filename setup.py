import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand
from codecs import open


here = os.path.abspath(os.path.dirname(__file__))

packages = ['carnet']

requires = [
    'blinker',
    'flask',
    'flask-bootstrap',
    'flask-flatpages',
    'flask-moment',
    'flask-script',
    'flask-wtf',
    'frozen-flask',
    'pygments'
]

test_requires = [
    'coverage',
    'docutils',
    'flake8',
    'flask-testing',
    'pytest',
    'pytest-cov',
    'sphinx',
    'tox'
]

entry_points = {
    'console_scripts': [
        'carnet = carnet.manage:main'
    ]
}

about = {}
with open(os.path.join(here, 'carnet', '__about__.py'), mode='r', encoding='utf-8') as f:
    exec(f.read(), about)

with open('README.rst', mode='r', encoding='utf-8') as f:
    readme = f.read()


class ToxTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    long_description=readme,
    packages=packages,
    install_requires=requires,
    test_requires=test_requires,
    cmdclass={'test': ToxTest},
    entry_points=entry_points,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
