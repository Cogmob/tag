import os
import fnmatch

def main():
    matches = []
    for root, dirnames, filenames in os.walk('src'):
        for filename in fnmatch.filter(filenames, '*.md'):
                matches.append(os.path.join(root, filename))
    for filename in matches:
        print(filename)
        print(change_extension(filename, 'html'))
        with open(filename) as f:
            print(f.read())


def change_extension(filename, new_extension):
    return filename

main()
