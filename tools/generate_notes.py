import os
import fnmatch
from subprocess import call

def main():
    lines = get_start()

    matches = []
    for root, dirnames, filenames in os.walk('.gen/src/notes'):
        for filename in fnmatch.filter(filenames, '*'):
                matches.append(os.path.join(root, filename))

    for filename in matches:
        call(['vim', '-c', 'set ft=txtfmt', '-c', 'TOhtml', '+wa', '+qa', filename])
        with open(filename + '.html') as f:
            lines += ['<details open>']
            lines += [get_title_line(filename)]
            lines += format_lines(get_content(f.read()))
            lines += ['</details>']

    lines += ['</body>']
    lines += ['</html>']

    with open('.gen/src/notes/index.html', 'w+') as f:
        f.write('\n'.join(lines))

def format_lines(lines):
    ret = []
    for line in lines:
        newline = format_title(format_bullet(line))
        ret += [newline]
    return ret

def change_extension(filename, old_extension, new_extension):
    return '%s.%s' % (filename.split('.'+old_extension)[0], new_extension)

def get_content(page):
    lines = page.split('\n')
    start = find_line_number(lines=lines, target='/style') + 1
    end = find_line_number(lines=lines, target='/body', start=start)
    return lines[start:end]

def find_line_number(lines, target, start=0):
    for i in range(start, len(lines)):
        if target in lines[i]:
            return i
    raise ValueError('target string not found')

def get_start():
    with open('tools/start.html', 'r') as f:
        return f.read().split('\n')
    raise IOError('start.html file missing')

def get_title_line(filename):
    return '<summary class="title0">' + filename.split('/')[-1] + '</summary>'

def format_title(line):
    if '>###' in line:
        newline = line.split('>###')
        return '<span class="title3">' + newline[1] + '</span>'
    if '>##' in line:
        newline = line.split('>##')
        return '<span class="title2">' + newline[1] + '</span>'
    if '>#' in line:
        newline = line.split('>#')
        return '<span class="title1">' + newline[1] + '</span>'
    return line

def format_bullet(line):
    return line.replace('>. ', '>• ').replace(' . ', ' • ')

main()
