#-*- coding: utf-8 -*-
import os
import re
import sys


# enumerate
for j, i in enumerate(open("変数説明byJc.txt")):
    # if re.search(r"変数名.+", i):
    if re.search(r"「.+", i):
    # if re.search(r"変数名.+", i):
        i=i.rstrip()
        print(j, i)
