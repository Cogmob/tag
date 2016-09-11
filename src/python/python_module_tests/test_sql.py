from compare import expect
from python.testing.test_decorator import with_setup_args
from nose.plugins.attrib import attr
import unittest

import sqlite3

def up():
    conn = sqlite3.connect(':memory:')
    conn.isolation_level = None
    cursor = conn.cursor()
    return [conn, cursor], {}

def down(conn, cursor):
    cursor.close()
    conn.close()

decorator = with_setup_args(up, down)

@decorator
def test_creating_tables(conn, cursor):
    cursor.execute('create table tableA (id INTEGER PRIMARY KEY);')
    cursor.execute('create table tableB (id INTEGER PRIMARY KEY);')
    res = cursor.execute('select name from sqlite_master where type = "table";')
    expect(res.fetchall()).to_equal([(u'tableA',), (u'tableB',)])
    return conn, cursor
