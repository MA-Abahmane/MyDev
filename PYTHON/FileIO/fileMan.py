#!/usr/bin/env python3

"""
File Manipulation
"""

f = open('file.txt', 'r')
ln = f.tell()
ln1 = f.readline()
ln2 = f.readlines()
f.seek(0)
ln3 = f.read()

'''
print(ln)
print(ln1)
print(ln2)
print(ln3)
'''


try:
    f = open('file.txt', 'x')
except FileExistsError:
    print('file Exists') 


f = open('file.txt', 'r+')

# Writing
f.write('line0\n')
f.writelines(['line1\n', 'line2\n', 'line3\n'])

# Seeker reset
f.seek(0)

# Reading
line = f.readline()
print(f'first line:\n{line}')

data = f.read()
print(f'data:\n{data}')