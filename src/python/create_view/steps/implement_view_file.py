def implement_view_file(view_file, existing_folder={}):
    if isinstance(view_file['folders'], list):
        print('has_folders')
    view_file['stored_files'] = [{'primary_tags': ['view']}]
    return view_file
