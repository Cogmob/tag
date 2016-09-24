from .implement_each import implement_each

def implement_view_file(view_file, existing_folder={}):
    if isinstance(view_file['folders'], dict):
        view_file['folders'] = {
                key: {'folders': {}, 'tags': val, 'files': val}
                for (key, val) in view_file['folders'].items()}
    view_file['stored_files'] = [{'primary_tags': ['view']}]
    if 'foreach' in view_file:
        for key, folder in view_file['folders'].items():
            folder[key] = implement_each(folder, view_file['foreach'])
    view_file.pop('foreach', None)
    return view_file
