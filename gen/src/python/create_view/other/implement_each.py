def implement_each(folder, each):
    folder['tags'] = each['tags'] + folder['tags']
    for key, tags in each['folders'].items():
        folder['folders'][key] = {'tags': tags, 'folders': {}}
    return folder
