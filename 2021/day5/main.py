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

#print(coordinates)