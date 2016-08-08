import os

gen_path = os.path.join(os.path.dirname(__file__), 'log/gen')
target_path = os.path.join(os.path.dirname(__file__), 'log/target')

def log_difference(a, b, message):
    print gen_path
    with open(gen_path, 'w') as gen_file:
        gen_file.write(message)
        gen_file.write(a)
    with open(target_path, 'w') as target_file:
        target_file.write(message)
        target_file.write(b)
    print 'log files written'
