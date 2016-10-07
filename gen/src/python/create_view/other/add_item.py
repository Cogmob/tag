from .tags_allowed import tags_allowed

def add_item(i, add_func):
    directory = i['directory']
    file_tags = i['file_tags']

    if not tags_allowed(directory['tags'], file_tags):
        return False, directory

    sub_folders_modified = False
    new_sub_folders = {}
    for key, sub_directory in directory['folders'].items():
        was_modified, new_sub_directory = add_item({
            'directory': sub_directory,
            'file_tags': file_tags}, add_func)
        if was_modified:
            if sub_folders_modified:
                raise ValueError('file was sorted into multiple subfolders')
            sub_folders_modified = True
        new_sub_folders[key] = new_sub_directory

    if sub_folders_modified:
        directory['folders'] = new_sub_folders
    else:
        directory = add_func(directory)

    return True, directory
