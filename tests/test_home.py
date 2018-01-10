import unittest

from flask_testing import TestCase

from tests.utils import (cleanup_folders, create_app_config, create_test_app,
                         delete_app_config)


class TestHome(TestCase):
    def create_app(self):
        return create_test_app()

    def tearDown(self):
        cleanup_folders()

    def test_page_not_found(self):
        rv = self.client.get('/unknown')
        self.assert_404(rv)
        self.assert_template_used('_themes/default/404.html')

    def test_pygments_css(self):
        rv = self.client.get('/pygments.css')
        self.assert_200(rv)

    def test_redirect_to_quickstart(self):
        delete_app_config()

        rv = self.client.get('/', follow_redirects=False)
        self.assert_redirects(rv, '/quickstart/')

        rv = self.client.get('/', follow_redirects=True)
        self.assert_200(rv)
        self.assert_template_used('quickstart.html')

    def test_empty_latest_posts(self):
        create_app_config()

        rv = self.client.get('/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/latest_posts.html')
        self.assert_context('posts', [])
        self.assert_context('post_page', 0)
        self.assert_context('post_page_max', 0)
        self.assertIn(b'No posts', rv.data)

    def test_empty_latest_posts_page_0(self):
        create_app_config()

        rv = self.client.get('/0/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/latest_posts_offset.html')
        self.assert_context('posts', [])
        self.assert_context('post_page', 0)
        self.assert_context('post_page_max', 0)
        self.assertIn(b'No posts', rv.data)


if __name__ == '__main__':
    unittest.main()
