def simplify(i, path=[]):
    files = []
    for stored_file in i['directory']['stored_files']:
        tags = [str(i) for i in stored_file['primary_tags'] if i not in path]
        files.append('__'.join(tags))

    return {
        'files': sorted(files)}
