import unittest

from flask_testing import TestCase
from carnet import create_app

from tests.utils import delete_app_config


class TestHome(TestCase):
    def create_app(self):
        app = create_app(config='testing')
        return app

    def test_redirect_to_quickstart(self):
        delete_app_config()

        rv = self.client.get('/', follow_redirects=False)
        self.assert_redirects(rv, '/quickstart/')

        rv = self.client.get('/', follow_redirects=True)
        self.assert_200(rv)
        self.assert_template_used('quickstart.html')


if __name__ == '__main__':
    unittest.main()
