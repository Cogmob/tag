from compare import expect
from python.module_tests.utils.with_setup_args import with_setup_args as s
from nose.plugins.attrib import attr
import unittest

import sqlite3
from create_database_for_tests import up, down
from python.does_database_match_yaml.does_database_match_yaml import does_database_match_yaml

@s(up, down)
def test_empty_table(conn, cursor):
    res = does_database_match_yaml(string='[]', conn=conn)
    expect(res).to_equal(True)
