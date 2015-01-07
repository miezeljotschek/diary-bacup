#!/usr/bin/env python
# -*- coding: utf-8 -*-
from html.parser import HTMLParser
import os

path = os.getcwd()
pjoin = os.path.join
path = pjoin(path, 'mypictures')
exists = os.path.exists
if not exists(path):
    os.mkdir(path)
pairs = {}

class LinkParser(HTMLParser):
    """
    Казалось бы лучший вариант, одно но: может попастся испорченная HTML
    страничка, и тогда LinkParser упадёт с ошибкой.
    """
    def __init__(self):
        super(LinkParser, self).__init__()
        self.num=0

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for name, value in attrs:
                if name == "src":
                    if value.startswith('file') or value == 'http://':
                        continue
                    if not value.startswith("http://"):
                        continue
                    print(value)
                    try:
                        try:
                            ext = value.split('.')[-1]
                            new_name = str(self.num) + '.'+ext
                            new_name = pjoin(path, new_name)
                        except Exception as e:
                            new_name = pjoin(path, 'new_name_'+str(self.num)+'.jpg')
                        #pairs.append((value, new_name))
                        pairs[value] = new_name
                    except Exception as e:
                        print("----------")
                        print(e)
                        print(value)
                        print("----------")
                    self.num += 1


fname = "diary.htm"
data = None
with open(fname, 'r', encoding="cp1251") as myf:
    data = myf.read()
LinkParser().feed(data)

with open('info.txt', 'w', encoding="utf-8") as myf:
    for url, path in pairs.items():
        #myf.write('{}\t{}\n'.format(url, path))
        myf.write(url)
        myf.write('\t')
        myf.write(path)
        myf.write('\n')

print('Finish!')