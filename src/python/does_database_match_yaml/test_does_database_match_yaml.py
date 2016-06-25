from compare import expect
from python.module_tests.utils.with_setup_args import with_setup_args as s
from nose.plugins.attrib import attr
import unittest
import os

import sqlite3
from python.initialise_database.create_database_for_tests import up, down
from does_database_match_yaml import does_database_match_yaml

@attr('s')
@s(up, down)
def test_does_database_match_yaml(conn, cursor):
    for test_name in get_test_names():
        try:
            expect(
                    does_database_match_yaml(string='[]', conn=conn)
                            ).to_equal(True)
        except:
            print test_name
            raise

def get_test_names():
    test_names = []
    for filename in os.listdir(
            "%s/test_data" % os.path.dirname(os.path.abspath(__file__))):
        if filename.endswith('.yaml'):
            test_names.append(filename[:-5])
