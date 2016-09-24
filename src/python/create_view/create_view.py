from simplads import Bundle, pipe, lift, add_first_data, pr, remove_data
from .steps.create_root import create_root
from .steps.add_files import add_files
from .steps.simplify import simplify

def create_view(view_files, example_files):
    return pipe(
        view_files,
        create_root,
        add_first_data('directory',
            'view_files', view_files,
            'files', example_files),
        # add sub folders
        remove_data('view_files'),
        add_files,
        remove_data('files'),
        simplify)
