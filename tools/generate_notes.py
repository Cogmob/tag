import glob
import sys

print(sys.version)

print 'working!'

with open('tools/generate_notes.py', 'r') as source:
    print source.read()

print ''
print ''
print ''
print ''

for filename in glob.iglog('src/notes/**', recursive=True):
    print(filename)
