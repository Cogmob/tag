from compare import expect
from nose.plugins.attrib import attr
import unittest
import os

import sqlite3
from python.initialise_database.create_database_for_tests import get_database_in_memory
from .does_database_match_yaml import does_database_match_yaml

def test_does_database_match_yaml():
    dirname = os.path.dirname(os.path.abspath(__file__))
    for test_name in get_names(dirname):
        with open('%s/test_data/%s.yaml' % (dirname, test_name)) as yaml:
            with open('%s/test_data/%s.sql' % (dirname, test_name)) as sql:
                try:
                    conn, cursor = get_database_in_memory()
                    for inst in sql:
                        conn.execute(inst)
                    expect(
                        does_database_match_yaml(string=yaml.read(), conn=conn)
                            ).to_equal(True)
                except:
                    print('test name: %s' % test_name)
                    raise

def get_names(dirname):
    test_names = []
    for filename in os.listdir("%s/test_data" % dirname):
        if filename.endswith('.yaml'):
            test_names.append(filename[:-5])
    return test_names
