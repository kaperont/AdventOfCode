import numpy as np

input = open("input.txt", "r").readlines()

coordinates = []
for line in input:
    line_list = line.split()
    coord1 = line_list[0].split(',')
    coord2 = line_list[-1].split(',')
    coordinates.append(list([coord1, coord2]))

coordinates = np.array(coordinates)

map = np.zeros((1000,1000), dtype=int)

for pair in coordinates:
    print("X:", pair[:,0])
    print("Y:", pair[:,1])

    xcoords = pair[:,0]
    ycoords = pair[:,1]

    for x in range(xcoords[1] - xcoords[0]):
        map[x] += 1
    
    for y in range(ycoords[1] - ycoords[0]):
        map[y] += 1

#print(coordinates)