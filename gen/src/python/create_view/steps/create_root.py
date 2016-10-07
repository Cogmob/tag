from python.create_view.other.implement_view_file import implement_view_file

def create_root(view_files):
    return {
        'directory': {
            'folders': {},
            'stored_files': [],
            'tags': ['file']},
        'view_files': view_files}

def create_root_r(view_files):
    if len(view_files) == 0:
        raise ValueError('root tag not found in any of the view files')

    view_file = view_files[0]
    if 'root' in view_file['tags']:
        return implement_view_file(view_file)
    return {
        'directory': create_root_r(view_files.pop(0)),
        'view_files': view_files}
