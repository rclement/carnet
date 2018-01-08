import unittest

from flask_testing import TestCase

from tests.utils import create_test_app, cleanup_folders


class TestHome(TestCase):

    def post_quickstart(self, data):
        return self.client.post(
            '/quickstart/',
            data=data,
            follow_redirects=True
        )

    def create_app(self):
        return create_test_app()

    def tearDown(self):
        cleanup_folders()

    def test_quickstart_empty(self):
        rv = self.post_quickstart({})
        self.assert200(rv)
        self.assert_template_used('quickstart.html')

    def test_quickstart_valid(self):
        rv = self.post_quickstart({
            'title': 'My Title',
            'subtitle': 'My subtitle',
            'author': 'Me Myself and I',
            'pages_path': 'pages',
            'posts_path': 'posts',
            'output_path': 'output',
        })
        self.assert_200(rv)
        self.assert_template_used('latest_posts.html')

    def test_quickstart_invalid(self):
        rv = self.post_quickstart({
            'title': '',
            'subtitle': '',
            'author': '',
            'pages_path': '',
            'posts_path': '',
            'output_path': '',
        })
        self.assert_200(rv)
        self.assert_template_used('quickstart.html')


if __name__ == '__main__':
    unittest.main()
