from epr import epr
from .or_tags_allowed import or_tags_allowed
from .and_tags_allowed import and_tags_allowed

def tags_allowed(tags, file_tags):
    return tags_allowed_r(tags, file_tags + ['file'])

def tags_allowed_r(tags, file_tags):
    if isinstance(tags, str):
        if tags in file_tags:
            return True
        return False

    if len(tags) is 1:
        return tags_allowed_r(tags[0], file_tags)

    instruction = tags[0]
    if instruction == 'or':
        return or_tags_allowed(tags[1:], file_tags, tags_allowed_r)
    if instruction == 'and':
        return and_tags_allowed(tags[1:], file_tags, tags_allowed_r)
    if instruction == 'not':
        return not tags_allowed_r(tags[1:], file_tags)

    epr(tags, 'red')
    raise ValueError('tags is not a string and does not contain an instruction')
