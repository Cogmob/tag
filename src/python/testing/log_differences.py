from compare import expect as compare_expect
import os

def mkdir_p(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

mkdir_p(os.path.join(os.path.dirname(__file__), 'log'))
gen_path = os.path.join(os.path.dirname(__file__), 'log/gen')
target_path = os.path.join(os.path.dirname(__file__), 'log/target')

def log_differences(a, b, message):
    print(gen_path)
    with open(gen_path, 'w+') as gen_file:
        gen_file.write(message)
        gen_file.write('\ngen:\n'+str(a))
    with open(target_path, 'w+') as target_file:
        target_file.write(message)
        target_file.write('\ntarget:\n' + str(b))
    print('log files written')

def expect(a):
    class r:
        def to_equal(self, b, message):
            if a != b:
                log_differences(a, b, message)
            compare_expect(a).to_equal(b)
    return r()
