#!/usr/bin/env python3
# -*- coding: utf-8 -*-
fname = 'info.txt'
folder_for_image = 'mypictures'
import urllib.request as r
import urllib.error
import time
import os

timeout = 2 # Timeout in secunds
path = os.getcwd()
pjoin = os.path.join
path = pjoin(path, folder_for_image)
exists = os.path.exists
if not exists(path):
    os.mkdir(path)

data = None
pairs = []
with open(fname, 'r', encoding="utf-8") as myf:
    #for url, path in pairs:
    #    myf.write('{}\t{}'.format(url, path))
    for line in myf:
        url, path = line.split('\t')
        path = path.strip()
        try:
            print(url)
            if exists(path):
                continue
            data = r.urlopen(url, timeout=timeout).read()
            with open(path, 'wb') as fl:
                fl.write(data)
            time.sleep(1)
        except urllib.error.HTTPError as e:
            print('Not found: {}'.format(url))
        except urllib.error.URLError as e:
            print("----------")
            print(e)
            print(url)
            print("----------")
        except Exception as e:
            print("----------")
            print(e)
            print(url)
            print("----------")

print('Finish!')