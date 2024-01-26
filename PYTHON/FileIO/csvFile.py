#!/usr/bin/env python3

"""
CSV - Comma Separated Values
"""

import csv


path = 'PYTHON/FileIO/files/data.csv'

fl = open(path, newline='')

writer = csv.reader(fl) # read file

header = next(writer) # get the first line (header)
data = [row for row in writer] # 

print(list(writer))
print(header)
print(data[0])


path = 'PYTHON/FileIO/files/data2.csv'
fl = open(path, 'w')
lst = [header, data[0], data[1], data[2]]
wrt = csv.writer(fl, delimiter=',', lineterminator='\n')

wrt.writerows(lst)
wrt.writerow(data[22])


