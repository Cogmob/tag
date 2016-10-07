def and_tags_allowed(tags, file_tags, tags_allowed_r):
    for tag in tags:
        if not tags_allowed_r(tag, file_tags):
            return False
    return True
