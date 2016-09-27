from .implement_each import implement_each

def implement_view_file(
        view_file,
        directory={'folders': {}, 'stored_files': []}):

    if isinstance(view_file['folders'], dict):
        for key, val in view_file['folders'].items():
            directory['folders'][key] = {
                    'folders': {},
                    'tags': val,
                    'files': val}

    directory['stored_files'].append([{'primary_tags': ['view']}])

    directory['files'].append(view_file['files'])
    epr(directory)

    if 'foreach' in view_file:
        for key, folder in view_file['folders'].items():
            directory['folders'][key] = implement_each(
                    directory['folders'][key], view_file['foreach'])

    return view_file
