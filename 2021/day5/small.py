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

    xcoords = pair[:,0]
    ycoords = pair[:,1]
    xcoords = [str(num) for num in xcoords]
    ycoords = [str(num) for num in ycoords]

    if xcoords[0] == xcoords[1]:
            
        y1 = int(ycoords[0])
        y2 = int(ycoords[1])
        x = int(xcoords[0])

        if y1 < y2:
            while y2 >= y1:
                map[y1][x] += 1
                y1 += 1
        elif y1 > y2:
            while y1 >= y2:
                map[y2][x] += 1
                y2 += 1
        else:
            continue

    elif ycoords[0] == ycoords[1]:

        x1 = int(xcoords[0])
        x2 = int(xcoords[1])
        y = int(ycoords[0])

        if x1 < x2:
            while x2 >= x1:
                map[y][x1] += 1
                x1 += 1
        elif x1 > x2:
            while x1 >= x2:
                map[y][x2] += 1
                x2 += 1
        else:
            continue
    
    else:
        # THE HARD STUFF...

        x1 = int(xcoords[0])
        x2 = int(xcoords[1])
        y1 = int(ycoords[0])
        y2 = int(ycoords[1])

        if x1 < x2:
            if y1 < y2:
                while (x2 >= x1) and (y2 >= y1):
                    map[y1][x1] += 1
                    x1 += 1
                    y1 += 1
            elif y1 > y2:
                while (x2 >= x1) and (y1 >= y2):
                    map[y1][x1] += 1
                    x1 += 1
                    y1 -= 1
        elif x1 > x2:
            if y1 < y2:
                while (x1 >= x2) and (y2 >= y1):
                    map[y1][x1] += 1
                    x1 -= 1
                    y1 += 1
            elif y1 > y2:
                while (x1 >= x2) and (y1 >= y2):
                    map[y1][x1] += 1
                    x1 -= 1
                    y1 -= 1
                    
print(map)

sum = 0
for row in map:
    for val in row:
        if int(val) > 1:
            sum += 1

print(sum)

    # for x in range(abs(xcoords[1] - xcoords[0]) + 2):
    #     for y in range(abs(ycoords[1] - ycoords[0]) + 2):
    #         map[x][y] += 1
    
    # for y in range(ycoords[1] - ycoords[0]):
    #     map[y] += 1

#print(coordinates)