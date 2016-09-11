from compare import expect
from python.testing.test_decorator import with_setup_args
from nose.plugins.attrib import attr
import unittest

from fs.opener import fsopendir

def up():
    app_fs = fsopendir('mount://src/python/testing/fs.ini', create_dir=True)
    app_fs.makedir('tmp/.tag')
    app_fs.makedir('tmp/.filtered')
    app_fs.makedir('tmp/example')
    app_fs.makedir('tmp/example/subdir')
    app_fs.createfile('tmp/example/file1')
    app_fs.createfile('tmp/example/file2')
    app_fs.createfile('tmp/example/subdir/file3')
    return [app_fs], {}

@with_setup_args(up)
def test_ls(app_fs):
    files = app_fs.listdir('tmp')
    expect(set(files)).to_equal(set(['example', '.tag', '.filtered']))

@with_setup_args(up)
def test_create_file(app_fs):
    files = app_fs.listdir('tmp')
    expect(set(files)).to_equal(set(['example', '.tag', '.filtered']))

@with_setup_args(up)
def test_create_several_files(app_fs):
    files = app_fs.listdir('tmp')
    expect(set(files)).to_equal(set(['example', '.tag', '.filtered']))
