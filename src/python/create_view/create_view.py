from simplads import Bundle, pipe, lift, add_data, pr, remove_data
from .steps.create_root import create_root
from .steps.add_files import add_files
from .steps.simplify import simplify
from .steps.add_view_files import add_view_files
from epr import epr

def create_view(view_files, example_files):
    return pipe(
        view_files,
        create_root,
        add_view_files,
        add_data('files', example_files),
        remove_data('view_files'),
        add_files,
        epr,
        remove_data('files'),
        simplify)
