import csv

# print("aaa")

with open("csv/iris.csv", 'r') as f:
    aa=f.read()

    print(len(aa))
    for i,j  in enumerate(f.read()):
        if i in range(10):
            print(j)
