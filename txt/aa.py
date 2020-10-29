import re
import sys


# file=input("aaa:")
file="dummy.txt"


# for i in open("dummy.txt"):
for i in open(file):
    i=i.rstrip()
    for word in i:
        print(word)
    # print(i)
