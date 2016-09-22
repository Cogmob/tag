from simplads import Bundle, pipe, lift, add_data, add_first_data
from .steps.create_root import create_root
from .steps.add_files import add_files
from .steps.simplify import simplify

def create_view(view_files, example_files):
    return pipe(
        view_files,
        create_root,
        add_first_data('directory',
            'files', example_files),
        add_files,
        simplify)
