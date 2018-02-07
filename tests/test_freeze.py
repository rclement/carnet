import unittest

from warnings import simplefilter as filter_warnings
from flask_frozen import MissingURLGeneratorWarning

from carnet import freezer

from .utils import TestAppConfigured


filter_warnings('ignore', MissingURLGeneratorWarning)


class TestFreezeConfigured(TestAppConfigured):

    def test_freeze(self):
        freezer.freeze()


if __name__ == '__main__':
    unittest.main()
