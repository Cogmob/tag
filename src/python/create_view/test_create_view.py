from compare import expect
from nose.plugins.attrib import attr
import unittest

import yaml
import os
from python.testing.glob_runner import glob_runner
from .create_view import create_view

src_path = os.path.dirname(os.path.abspath(__file__))

def each_create_view(data):
    with open(data['filename']) as viewfile:
        view_files = yaml.load(viewfile.read())
        res = create_view(view_files, example_files)
        with open(data['filename'].split('.view')[0] + '.files') as files:
            expect(res).to_equal(yaml.load(files.read()))

@attr('s')
def test_create_view():
    glob_runner(
        glob_array = [src_path, 'data', '[0-10]*.tag'],
        func = each_create_view,
        root_path_array = [src_path, 'data'],
        white_list = ['02'])

def get_example_files():
    with open(os.path.join(src_path, 'data', 'files')) as files:
        return yaml.load(files.read())

example_files = get_example_files()
