from simplads import Bundle, pipe, lift, add_data, add_first_data, pr
from .steps.create_root import create_root
from .steps.add_files import add_files
from .steps.simplify import simplify
import pprint
pp = pprint.PrettyPrinter(indent=4)

def pri(i):
    print(pprint.pprint(i, indent=4))
    return i

def create_view(view_files, example_files):
    return pipe(
        view_files,
        create_root,
        add_first_data('directory',
            'files', example_files),
        pri,
        add_files,
        simplify)
