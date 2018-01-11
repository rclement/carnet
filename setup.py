import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from codecs import open


here = os.path.abspath(os.path.dirname(__file__))

packages = find_packages()

requires = [
    'blinker',
    'flask',
    'flask-bootstrap',
    'flask-flatpages',
    'flask-moment',
    'flask-script',
    'flask-themes',
    'flask-wtf',
    'frozen-flask',
    'pygments'
]

tests_require = [
    'docutils',
    'tox'
]

dependency_links = [
    'https://github.com/rclement/flask-themes.git@fix-integration-flask-0.12#egg=flask-themes'
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
    dependency_links=dependency_links,
    tests_require=tests_require,
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
