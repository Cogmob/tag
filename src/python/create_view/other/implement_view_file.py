from .implement_each import implement_each

def implement_view_file(
        view_file,
        directory = {'folders': {}, 'stored_files': []}):

    if isinstance(view_file['folders'], dict):
        for key, val in view_file['folders'].items():
            directory['folders'][key] = {
                    'folders': {},
                    'tags': val}

    if 'stored_file' not in directory:
        directory['stored_files'] = []
    directory['stored_files'].append({'primary_tags': ['view']})

    directory['tags'] += view_file['tags']

    if 'foreach' in view_file:
        for key, folder in view_file['folders'].items():
            directory['folders'][key] = implement_each(
                    directory['folders'][key], view_file['foreach'])

    return directory
