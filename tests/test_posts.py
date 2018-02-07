import unittest

from .utils import (TestAppConfigured, TestAppNotConfigured)


class TestPostsConfigured(TestAppConfigured):

    def test_empty_all_posts(self):
        rv = self.client.get('/posts/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/posts.html')
        self.assert_context('posts', [])
        self.assertIn(b'No posts', rv.data)

    def test_unknown_post(self):
        rv = self.client.get('/posts/unknown/')
        self.assert_404(rv)
        self.assert_template_used('_themes/default/404.html')


class TestPostsNotConfigured(TestAppNotConfigured):

    def test_redirect_to_quickstart(self):
        rv = self.client.get('/posts/', follow_redirects=False)
        self.assert_redirects(rv, '/quickstart/')

        rv = self.client.get('/posts/', follow_redirects=True)
        self.assert_200(rv)
        self.assert_template_used('quickstart.html')


if __name__ == '__main__':
    unittest.main()
