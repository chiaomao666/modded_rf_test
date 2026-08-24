from pathlib import Path
import difflib
import sys

file1 = Path(r"c:\Users\wuser\Desktop\2.28\assets\static\js\bj = function(e)_ori.js")
file2 = Path(r"c:\Users\wuser\Desktop\2.28\assets\static\js\bj = function(e).js")

text1 = file1.read_text(encoding='utf-8')
text2 = file2.read_text(encoding='utf-8')

lines1 = text1.splitlines()
lines2 = text2.splitlines()

print('FILE1_LINES', len(lines1))
print('FILE2_LINES', len(lines2))
print('--- DIFF ---')
for line in difflib.unified_diff(lines1, lines2, fromfile=str(file1.name), tofile=str(file2.name), lineterm=''):
    print(line)

print('\n--- CHANGED_LINE_SUMMARY ---')
# simple line-by-line comparison ignoring blank lines and whitespace-only changes
for i, (a, b) in enumerate(zip(lines1, lines2), 1):
    if a != b:
        print(f'line {i}:')
        print('  ori :', a)
        print('  new :', b)

# if one file longer, print extra lines
for i in range(min(len(lines1), len(lines2)) + 1, max(len(lines1), len(lines2)) + 1):
    if i <= len(lines1):
        print(f'line {i} only in ori: {lines1[i-1]}')
    if i <= len(lines2):
        print(f'line {i} only in new: {lines2[i-1]}')
