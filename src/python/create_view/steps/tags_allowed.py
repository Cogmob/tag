def tags_allowed(tags, file_tags):
    if 'file' in tags or 'root' in tags:
        return True
    for tag in tags:
        if tag in file_tags['primary_tags']:
            return True
        if tag in file_tags['secondary_tags']:
            return True
    return False
