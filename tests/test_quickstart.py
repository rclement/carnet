import unittest

from tests.utils import TestAppNotConfigured


class TestQuickstart(TestAppNotConfigured):

    def post_quickstart(self, data):
        return self.client.post(
            '/quickstart/',
            data=data,
            follow_redirects=True
        )

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
        self.assert_template_used('_themes/default/index.html')

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
