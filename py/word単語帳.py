import csv
import random
#
file="aa.csv"

list_data=[]

with open(file, "r") as f:
    reader=csv.reader(f)

    for i in reader:
        list_data.append(i)

# print(list_data)

num=random.randint(0, len(list_data)-1)



conti="q"

while(conti=="q"):
    print(list_data[num][0])
    check=input("want to know answer? ")
    if check=="q":
        print(list_data[num][1])

    conti=input("continue?")
