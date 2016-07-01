from compare import expect
from python.module_tests.utils.with_setup_args import with_setup_args as s
from nose.plugins.attrib import attr
import unittest
import os
import yaml

from fs.opener import fsopendir

def up():
    app_fs = fsopendir('mount://src/python/module_tests/data/fs.ini', create_dir=True)
    return [app_fs], {}

@attr('s')
@s(up)
def test_create_files_from_yaml(app_fs):
    dirname = os.path.dirname(os.path.abspath(__file__))
    for test_name in get_test_names(dirname):
        try:
            with open('%s/test_data/%s' % (dirname, test_name)) as f:
                files = yaml.load(f.read())
                print files
        except:
            print 'test failed in: test_create_files_from_yaml.py'
            print 'test name: %s' % test_name
            raise
    expect(1).to_equal(2)

def get_test_names(dirname):
    return [i for i in os.listdir("%s/test_data" % dirname) if i[0] is not '.']
