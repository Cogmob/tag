from compare import expect
from nose.plugins.attrib import attr
import unittest

def test_if_this_test_can_be_selected():
    expect(1).to_equal(1)

def test_basic_assert():
    assert True
