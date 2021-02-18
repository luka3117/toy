def aaa(file):

    import csv
    lines=[]
    # with open("iris.csv", "r") as f:
    with open(str(file), "r") as f:
        file=csv.reader(f)
        for i in file:
            x1, x2, x3, x4, x5 = i
            line=[x1, x2, x3, x4, x5]
            # x1, x2 = i
            # line=[x1, x2]
            lines.append(line)
    f.close()
    return lines

# print(aaa("iris.csv"))
aaa=aaa("aaa.csv")
aaa
print()
# print(lines)
