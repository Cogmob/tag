from .add_file import add_file

def add_files(i):
    directory = i['directory']
    files = i['files']

    for file_tags in files:
        added, directory = add_file({
            'directory': directory,
            'file_tags': file_tags})
        if not added:
            raise ValueError('file was not added')
    return {
        'directory': directory,
        'files': files}
