import unittest

from datetime import date

from tests.utils import (TestAppConfigured, TestAppNotConfigured)


class TestArchivesConfigured(TestAppConfigured):

    def test_empty_all_archives(self):
        rv = self.client.get('/archives/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/archives.html')
        self.assert_context('archives', [])
        self.assertIn(b'No tags', rv.data)

    def test_empty_yearly_archives(self):
        year = 2018
        rv = self.client.get('/archives/' + str(year) + '/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/archives_yearly.html')
        self.assert_context('archive_date', date(year=year, month=1, day=1))
        self.assert_context('posts', [])

    def test_empty_monthly_archives(self):
        year = 2018
        month = 1
        rv = self.client.get('/archives/' + str(year) + '/' + str(month) + '/')
        self.assert_200(rv)
        self.assert_template_used('_themes/default/archives_monthly.html')
        self.assert_context('archive_date', date(year=year, month=month, day=1))
        self.assert_context('posts', [])


class TestArchivesNotConfigured(TestAppNotConfigured):

    def test_redirect_to_quickstart(self):
        rv = self.client.get('/categories/', follow_redirects=False)
        self.assert_redirects(rv, '/quickstart/')

        rv = self.client.get('/categories/', follow_redirects=True)
        self.assert_200(rv)
        self.assert_template_used('quickstart.html')


if __name__ == '__main__':
    unittest.main()
