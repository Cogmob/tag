from .implement_view_file import implement_view_file

def create_root(view_files):
    if len(view_files) == 0:
        raise ValueError('root tag not found in any of the view files')

    view_file = view_files[0]
    if 'root' in view_file['tags']:
        return implement_view_file(view_file)
    return create_root(view_files.pop(0))
