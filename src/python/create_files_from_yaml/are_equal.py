import json
from python.module_tests.log_difference import log_difference

def are_equal(a, b, message=''):
    if are_equal_recursive(a, b) and are_equal_recursive(b, a):
        return True
    else:
        log_difference(
                json.dumps(a, indent=4, sort_keys=True),
                json.dumps(b, indent=4, sort_keys=True),
                message=message)
        return False

def are_equal_recursive(a, b):
    if isinstance(a, str):
        return a == b

    for key, val in a.items():
        if key not in b:
            return False
        if not are_equal_recursive(a[key], b[key]):
            return False
    return True
