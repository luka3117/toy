#-*- coding: utf-8 -*-
import os
import re
import sys


output=open("aaaa.txt", mode='w')

for i in open("h.txt"):
    if "the" in i:
        print(i)
    # if  __name__ == "__main__":
    #     if "the" in i:
    #         print(i)
    # else :
    #     if "the" in i:
    #         print(i, file=output)
