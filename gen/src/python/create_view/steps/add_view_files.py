from termcolor import colored
from python.create_view.other.add_item import add_item
from python.create_view.other.get_add_view_file_func import get_add_view_file_func

def add_view_files(i):
    directory = i['directory']
    view_files = i['view_files']

    for view_file in view_files:
        added, directory = add_item({
                'directory': directory,
                'file_tags': view_file['tags']},
            get_add_view_file_func(view_file))
        if not added:
            raise ValueError('view_file not added')

    return {
        'directory': directory}
