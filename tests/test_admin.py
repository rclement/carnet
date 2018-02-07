import unittest

from .utils import TestAppConfigured, TestAppNotConfigured


class TestCategoriesConfigured(TestAppConfigured):

    def test_admin_dashboard(self):
        rv = self.client.get('/admin/')
        self.assert_200(rv)
        self.assert_template_used('admin.html')

    def test_admin_posts(self):
        rv = self.client.get('/admin/')
        self.assert_200(rv)
        self.assert_template_used('admin.html')

    def test_admin_pages(self):
        rv = self.client.get('/admin/')
        self.assert_200(rv)
        self.assert_template_used('admin.html')


class TestHomeNotConfigured(TestAppNotConfigured):

    def test_redirect_to_quickstart(self):
        rv = self.client.get('/', follow_redirects=False)
        self.assert_redirects(rv, '/quickstart/')

        rv = self.client.get('/', follow_redirects=True)
        self.assert_200(rv)
        self.assert_template_used('quickstart.html')


if __name__ == '__main__':
    unittest.main()
