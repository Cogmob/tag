def create_yaml_from_files(fs):
    return create_dict_from_dir(fs)

def create_dict_from_dir(fs):
    folders = {}
    files = {}
    for path in fs.ilistdir():
        if fs.isdir(path):
            folders[path] = create_dict_from_dir(fs.opendir(path))
        else:
            files[path] = fs.getcontents(path)
    ret = {}
    if len(folders) > 0:
        ret['folders'] = folders
    if len(files) > 0:
        ret['files'] = files
    return ret
