from compare import expect
from with_setup_args import with_setup_args
from nose.plugins.attrib import attr
import unittest

import os
import pyfakefs.fake_filesystem as fake_fs

def setup():
    fs = fake_fs.FakeFilesystem(path_separator='/')
    os = fake_fs.FakeOsModule(fs)
    return [fs, os], {}

def tear_down(fs, os):
    pass

@with_setup_args(setup, tear_down)
def test_create_a_file(fs, os):
    fs.CreateFile('test-file.txt')
    files = os.listdir('.')
    expect(files).to_equal(['test-file.txt'])
