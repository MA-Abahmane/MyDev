#!/usr/bin/python3

"""
Regular Expression
"""

import re


strns = ['Kiwi', 'Mango', 'Apple', 'Banana', 'Aki',
        'Orange', 'Avocado', 'Pineapple', 'Watermelon']

regex = '^A'
for s in strns:

    matches = re.search(regex, s)
    if matches:
        print(s)


strns = 'The Battle of Uhud on 23 March 625'

regex = '\d+\s\w+\s\d+'

matche = re.findall(regex, strns)

print(matche)

matche1 = re.findall(r'\d$', strns)
matche2 = re.findall(r'\d\Z', strns)

matche3 = re.findall(r'\bU\w+', strns)
matche4 = re.search(r'\s\b[A-Z]', strns)

split = re .split('\s', strns, 2)
sub = re.sub('\s', '-', strns, 2)

print(matche1)
print(matche2)
print(matche3)
print(matche4.group(0))
print(split)
print(sub)