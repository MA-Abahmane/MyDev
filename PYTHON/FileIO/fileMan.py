#!/usr/bin/env python3

"""
File Manipulation
"""

f = open('file.txt', 'r')
ln = f.tell()
ln1 = f.readline()
ln2 = f.readlines()
ln3 = f.read()

'''
print(ln)
print(ln1)
print(ln2)
print(ln3)
'''


f = open('file.txt', 'w')
f.write('hello\n')
f.writelines(['1Line\n', '2Line\n', '\n', '4Line\n'])


f = open('file.txt', 'a')
f.write('0ADD\n')
f.writelines(['1ADD\n', '2ADD\n', '\n', '4ADD\n'])


try:
    f = open('file.txt', 'x')
except FileExistsError:
    print('file Exists') 
