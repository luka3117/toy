#-*- coding: utf-8 -*-
import os;import re;import sys


# ussage :
# python jcombine.py ".py" "aa.txt"

# assing file kind
# kind=".txt"
kind=sys.argv[1]

# no asking exsistence of folder
os.system("mkdir -p res")


# assing output file name
# out_file_name="ttt.txt"
out_file_name= sys.argv[2]

out_file_path="./res/"

out_file_full_path_name = out_file_path + out_file_name


files=[i for i in os.listdir() if kind in i ]

output=open(out_file_full_path_name, "w", encoding="utf_8")

# file=files[0]

for file in files:
    for i in open(file):
        print(file, i.rstrip(), file=output)
