import json
<<<<<<< HEAD
#from python.testing.log_difference import log_difference
=======
from python.testing.log_differences import log_differences
>>>>>>> 91aeb195db7618d3a190eab50d6657a754984229

def are_equal(a, b, message=''):
    if are_equal_recursive(a, b) and are_equal_recursive(b, a):
        return True
    else:
<<<<<<< HEAD
#        log_difference(
#                json.dumps(a, indent=4, sort_keys=True),
#                json.dumps(b, indent=4, sort_keys=True),
#                message=message)
=======
        log_differences(
                json.dumps(a, indent=4, sort_keys=True),
                json.dumps(b, indent=4, sort_keys=True),
                message=message)
>>>>>>> 91aeb195db7618d3a190eab50d6657a754984229
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
