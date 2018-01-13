import unittest

from tests.utils import (TestAppConfigured, TestAppNotConfigured)


class TestHomeConfigured(TestAppConfigured):

    def test_page_not_found(self):
        rv = self.client.get('/unknown')
        self.assert_404(rv)
        self.assert_template_used('_themes/default/404.html')

    def test_pygments_css(self):
        rv = self.client.get('/pygments.css')
        self.assert_200(rv)

    def test_empty_latest_posts(self):
        rv = self.client.get('/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/index.html')
        self.assert_context('posts', [])
        self.assert_context('post_page', 0)
        self.assert_context('post_page_max', 0)
        self.assertIn(b'No posts', rv.data)

    def test_empty_latest_posts_page_0(self):
        rv = self.client.get('/0/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/index.html')
        self.assert_context('posts', [])
        self.assert_context('post_page', 0)
        self.assert_context('post_page_max', 0)
        self.assertIn(b'No posts', rv.data)


class TestHomeNotConfigured(TestAppNotConfigured):

    def test_redirect_to_quickstart(self):
        rv = self.client.get('/', follow_redirects=False)
        self.assert_redirects(rv, '/quickstart/')

        rv = self.client.get('/', follow_redirects=True)
        self.assert_200(rv)
        self.assert_template_used('quickstart.html')


if __name__ == '__main__':
    unittest.main()
