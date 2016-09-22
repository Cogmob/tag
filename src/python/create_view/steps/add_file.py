from .tags_allowed import tags_allowed

def add_file(i):
    directory = i['directory']
    file_tags = i['file_tags']

    if not tags_allowed(directory['tags'], file_tags):
        return False, directory

    sub_folders_modified = False
    new_sub_folders = []
    for sub_directory in directory['folders']:
        was_modified, new_sub_directory = add_file(sub_directory, file_tags)
        if was_modified:
            if sub_folders_modified:
                raise ValueError('file was sorted into multiple subfolders')
            sub_folders_modified = True
        new_sub_folders.push(new_sub_directory)

    if sub_folders_modified:
        directory['folders'] = new_sub_folders
    else:
        if 'stored_files' not in directory:
            directory['stored_files'] = []
        directory['stored_files'].append(file_tags)

    return True, directory
