from python.create_view.other.get_add_file_func import get_add_file_func
from python.create_view.other.add_item import add_item

def add_files(i):
    directory = i['directory']
    files = i['files']

    for file_tags in files:
        tags = file_tags['primary_tags'] + file_tags['secondary_tags']
        tags.append('file')
        tags.append('root')
        added, directory = add_item({
            'directory': directory,
            'file_tags': tags},
            get_add_file_func(file_tags))
        if not added:
            raise ValueError('file was not added')
    return directory
