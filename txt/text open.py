#-*- coding: utf-8 -*-

"""
一括変換コード
10月30日(金)
"""

import os
import re
import sys

InputFile=input("テキスト名を入力：")
InputFile=open(InputFile)

# for i in open("111.txt"):
for i in InputFile:
    i=i.rstrip()
    i=re.sub(r"\.", r".\n", i)
    print(i)
