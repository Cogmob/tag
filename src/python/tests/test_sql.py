from compare import expect
from with_setup_args import with_setup_args as s
from nose.plugins.attrib import attr
import unittest

import sqlite3

def up():
    conn = sqlite3.connect(':memory:')
    conn.isolation_level = None
    c = conn.cursor()
    return [c], {}

@s(up)
def test_creating_tables(c):
    c.execute('create table tableA (id INTEGER PRIMARY KEY);')
    c.execute('create table tableB (id INTEGER PRIMARY KEY);')
    res = c.execute('select name from sqlite_master where type = "table";')
    expect(res.fetchall()).to_equal([(u'tableA',), (u'tableB',)])
