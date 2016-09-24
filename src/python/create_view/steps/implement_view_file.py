def implement_view_file(view_file, existing_folder={}):
    if isinstance(view_file['folders'], dict):
        view_file['folders'] = {
                key: {'folders': {}, 'tags': val, 'files': val}
                for (key, val) in view_file['folders'].items()}
    view_file['stored_files'] = [{'primary_tags': ['view']}]
    return view_file
