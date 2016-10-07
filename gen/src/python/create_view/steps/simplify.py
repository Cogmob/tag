def simplify(i, path=[]):
    ret = {}

    folders = {}
    for key, folder in i['folders'].items():
        simplified = simplify(folder, path + folder['tags'])
        if 'files' in simplified or 'folders' in simplified:
            folders[key] = simplified
    if len(folders) > 0:
        ret['folders'] = folders

    files = []
    if 'stored_files' in i:
        for stored_file in i['stored_files']:
            tags = [str(i) for i in stored_file['primary_tags'] if i not in path]
            files.append('__'.join([i for i in tags if i not in path]))
        if len(files) > 0:
            ret['files'] = sorted(files)
            # story - superhero can see future but only if make bad thing happen

    return ret
