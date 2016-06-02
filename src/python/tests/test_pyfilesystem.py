from compare import expect
from utils.with_setup_args import with_setup_args as s
from nose.plugins.attrib import attr
import unittest

from fs.opener import fsopendir

def up():
    app_fs = fsopendir('mount://src/python/tests/data/fs.ini', create_dir=True)
    app_fs.makedir('tmp/.tagger')
    app_fs.makedir('tmp/.filtered')
    return [app_fs], {}

@s(up)
def test_ls(app_fs):
    files = app_fs.listdir('tmp')
    expect(files).to_equal(['.tagger', '.filtered'])
