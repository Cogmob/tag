def tags_allowed(tags, file_tags):
    if 'file' in tags:
        return True
    for tag in tags:
        if tag in file_tags:
            return True
    return False
