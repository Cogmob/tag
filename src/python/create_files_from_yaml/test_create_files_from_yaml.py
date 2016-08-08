from compare import expect
from python.module_tests.utils.with_setup_args import with_setup_args as s
from nose.plugins.attrib import attr
import unittest
import os
import yaml

from fs.opener import fsopendir
from python.create_files_from_yaml.create_files_from_yaml import create_files_from_yaml
from python.create_files_from_yaml.create_yaml_from_files import create_yaml_from_files
from python.create_files_from_yaml.are_equal import are_equal

def up():
    app_fs = fsopendir('mount://src/python/module_tests/data/fs.ini', create_dir=True)
    return [app_fs.opendir('tmp')], {}

@attr('s')
@s(up)
def test_create_files_from_yaml(app_fs):
    dirname = os.path.dirname(os.path.abspath(__file__))
    for test_name in get_test_names(dirname):
        try:
            with open('%s/test_data/%s' % (dirname, test_name)) as f:
                before = yaml.load(f.read())
                create_files_from_yaml(app_fs, before)
                after = create_yaml_from_files(app_fs)
                expect(are_equal(before, after)).to_equal(True)
        except:
            print 'test failed in: test_create_files_from_yaml.py'
            print 'test name: %s' % test_name
            raise

def get_test_names(dirname):
    return [i for i in os.listdir("%s/test_data" % dirname) if i[0] is not '.']
