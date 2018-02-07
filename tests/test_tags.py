import unittest

from .utils import (TestAppConfigured, TestAppNotConfigured)


class TestTagsConfigured(TestAppConfigured):

    def test_empty_all_tags(self):
        rv = self.client.get('/tags/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/tags.html')
        self.assert_context('tags', [])
        self.assertIn(b'No tags', rv.data)

    def test_unknown_tag(self):
        rv = self.client.get('/tags/unknown/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/tag.html')
        self.assert_context('pages', [])
        self.assert_context('posts', [])


class TestTagsNotConfigured(TestAppNotConfigured):

    def test_redirect_to_quickstart(self):
        rv = self.client.get('/tags/', follow_redirects=False)
        self.assert_redirects(rv, '/quickstart/')

        rv = self.client.get('/tags/', follow_redirects=True)
        self.assert_200(rv)
        self.assert_template_used('quickstart.html')


if __name__ == '__main__':
    unittest.main()
