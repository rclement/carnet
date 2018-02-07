import unittest

from .utils import (TestAppConfigured, TestAppNotConfigured)


class TestPagesConfigured(TestAppConfigured):

    def test_empty_all_pages(self):
        rv = self.client.get('/pages/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/pages.html')
        self.assert_context('pages', [])
        self.assertIn(b'No pages', rv.data)

    def test_unknown_page(self):
        rv = self.client.get('/pages/unknown/')
        self.assert_404(rv)
        self.assert_template_used('_themes/default/404.html')


class TestPagesNotConfigured(TestAppNotConfigured):

    def test_redirect_to_quickstart(self):
        rv = self.client.get('/pages/', follow_redirects=False)
        self.assert_redirects(rv, '/quickstart/')

        rv = self.client.get('/pages/', follow_redirects=True)
        self.assert_200(rv)
        self.assert_template_used('quickstart.html')


if __name__ == '__main__':
    unittest.main()
