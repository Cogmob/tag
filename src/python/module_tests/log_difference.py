import os

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

mkdir_p(os.path.join(os.path.dirname(__file__), 'log'))
gen_path = os.path.join(os.path.dirname(__file__), 'log/gen')
target_path = os.path.join(os.path.dirname(__file__), 'log/target')

def log_difference(a, b, message):
    print(gen_path)
    with open(gen_path, 'w+') as gen_file:
        gen_file.write(message)
        gen_file.write('gen:\n'+a)
    with open(target_path, 'w+') as target_file:
        target_file.write(message)
        target_file.write('target:\n' + b)
    print('log files written')
