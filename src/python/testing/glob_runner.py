import os
from glob import glob

def glob_runner(
        glob_array = None,
        func = None,
        white_list = None,
        black_list = None,
        root_path_array = None):

    # incorrect arguments
    if glob_array is None:
        raise ValueError(
            'must have glob_array eg [\'c://my_docs\', \'doc[1-3]\']')
    if func is None:
        raise ValueError(
            'must have func which takes {root_path, filename} argument')


    glob_path = os.path.join(*glob_array)

    filenames = glob(glob_path)

    if root_path_array is not None:
        root_path = os.path.join(*root_path_array)
        filenames = [i.split(root_path)[1][1:] for i in filenames]

    if white_list is not None:
        filenames = filter_whitelist(white_list, filenames)

    if black_list is not None:
        filenames = filter_blacklist(black_list, filenames)

    for filename in filenames:
        data = {
                'root_path': root_path,
                'local_filename': filename}
        func(data)

def filter_whitelist(white_list, filenames, ret=[]):
    if len(filenames) is 0:
        return ret
    if is_listed(white_list, filenames[-1]):
        return filter_whitelist(white_list, filenames[:-1], ret + [filenames[-1]])
    return filter_whitelist(white_list, filenames[:-1], ret)

def is_listed(white_list, filename):
    if len(white_list) is 0:
        return False
    if white_list[-1] in filename:
        return True
    return is_listed(white_list[:-1], filename)

def filter_blacklist(black_list, filenames, ret=[]):
    if len(filenames) is 0:
        return ret
    if is_listed(black_list, filenames[-1]):
        return filter_blacklist(black_list, filenames[:-1], ret)
    return filter_blacklist(black_list, filenames[:-1], ret + [filenames[-1]])
