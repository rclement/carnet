import unittest

from tests.utils import (TestAppConfigured, TestAppNotConfigured)


class TestCategoriesConfigured(TestAppConfigured):

    def test_empty_all_categories(self):
        rv = self.client.get('/categories/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/categories.html')
        self.assert_context('categories', [])
        self.assertIn(b'No tags', rv.data)

    def test_unknown_category(self):
        rv = self.client.get('/categories/unknown/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/category.html')
        self.assert_context('pages', [])
        self.assert_context('posts', [])


class TestCategoriesNotConfigured(TestAppNotConfigured):

    def test_redirect_to_quickstart(self):
        rv = self.client.get('/categories/', follow_redirects=False)
        self.assert_redirects(rv, '/quickstart/')

        rv = self.client.get('/categories/', follow_redirects=True)
        self.assert_200(rv)
        self.assert_template_used('quickstart.html')


if __name__ == '__main__':
    unittest.main()
