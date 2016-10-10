from nose.plugins.attrib import attr
from python.testing.log_differences import expect
import unittest

import traceback
import yaml
import os
from python.testing.glob_runner import glob_runner
from .create_view import create_view

src_path = os.path.dirname(os.path.abspath(__file__))

@attr('s')
def test_create_view():
    glob_runner(
        glob_array = [src_path, 'data', '[0-10]*.tag'],
        func = each_create_view,
        root_path_array = [src_path, 'data'],
        white_list = ['02'])

def each_create_view(data):
    with open(data['filename']) as viewfile:
        view_files = yaml.load(viewfile.read())
        try:
            res = create_view(view_files, example_files)
        except Exception as ex:
            res = ''.join(
                    traceback.format_exception(
                        etype=type(ex),value=ex,tb=ex.__traceback__))
        with open(data['filename'].split('.view')[0] + '.files') as files:
            m = data['filename']
            expect(res).to_equal(yaml.load(files.read()), m)

def get_example_files():
    with open(os.path.join(src_path, 'data', 'files')) as files:
        return yaml.load(files.read())

example_files = get_example_files()
