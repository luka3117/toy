import csv
coords = []
# with open(f'{file_name}.csv', 'r') as csvFile:
with open("aaa.csv", 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        x,y = row
        coord = [float(x),float(y)]
        coords.append(coord)
csvFile.close()

print(coords)
return coords

def get_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x,y = row
            coord = [float(x),float(y)]
            coords.append(coord)
    csvFile.close()
    return coords

    # import csv

 # get_coords_from_csv("aaa.csv")
get_coords_from_csv("aaa")

print(get_coords_from_csv("aaa"))





# get_coords_from_csv("iris.csv")




# with open("iris.csv") as f:
#     a=csv.reader(f)
#     for i in a:
#         print(i)
