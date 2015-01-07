#!/usr/bin/env python3
# -*- coding: utf-8 -*-
fname = "diary.htm"
new_fname = "diary2.htm"
import os

data = None
pairs = []
base = os.getcwd()
sep = os.path.sep
with open('info.txt', 'r', encoding="utf-8") as myf:
    #for url, path in pairs:
    #    myf.write('{}\t{}'.format(url, path))
    for line in myf:
        url, path = line.split('\t')
        path = path.strip()
        path = path.replace(base, '')
        if path.startswith(sep):
            path = path.replace(sep, '', 1)
        pairs.append((url, path))

with open(fname, 'r', encoding="cp1251") as myf:
    data = myf.read()
    print("Len of data", len(data))
    print(type(data))

for url, path in pairs:
    data = data.replace(url, path)
    print('Replace: {} to {}\n'.format(url, path))

with open(new_fname, 'w', encoding="cp1251") as myf:
    myf.write(data)

print('Finish!')
