#!/usr/bin/python3

import json


data1 = {'id': 770, 'name': 'MAA'}
data2 = {'id': 771, 'name': 'CNN'}


fl = open('file.json', 'r+')
if fl.read() == '':
    json.dump({'Data':[]}, fl)

fl = open('file.json', 'r')
json_data = json.loads(fl.read()) 


json_data['Data'].append(data1)

fl = open('file.json', 'w+')
json.dump(json_data, fl)



fl = open('file.json', 'r')

d1 = json.loads(fl.read())
print(d1)

