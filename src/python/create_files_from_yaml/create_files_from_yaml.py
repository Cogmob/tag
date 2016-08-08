def create_files_from_yaml(fs, files):
    create_files(fs, files)

def create_files(fs, files):
    if 'folders' in files:
        for child_folder_name, data in files['folders'].iteritems():
            fs.makedir(child_folder_name)
            create_files(fs.opendir(child_folder_name), data)

    if 'files' in files:
        for child_file_name, data in files['files'].iteritems():
            fs.setcontents(child_file_name, data)
