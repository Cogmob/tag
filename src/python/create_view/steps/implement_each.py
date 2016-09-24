def implement_each(folder, each):
    folder['tags'] += each['tags']
    folder['files'] += each['files']
    for key, tags in each['folders'].items():
        folder['folders'][key] = {'files': tags, 'tags': tags, 'folders': {}}
    return folder