from compare import expect
from nose.plugins.attrib import attr
import unittest

class TestNoserunner(unittest.TestCase):
    @attr('example')
    def test_if_this_test_can_be_selected(self):
        expect(1).to_equal(1)

    def test_basic_assert(self):
        assert True
