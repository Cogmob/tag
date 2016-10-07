def or_tags_allowed(tags, file_tags, tags_allowed_r):
    for tag in tags:
        if tags_allowed_r(tag, file_tags):
            return True
    return False
