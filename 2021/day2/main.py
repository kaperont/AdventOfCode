input = open("input.txt", "r").readlines()

horizontal = 0
depth = 0
aim = 0

for line in input:
    direction, value = line.split()

    if direction == "forward":
        horizontal += int(value)
        depth += aim*int(value)

    elif direction == "up":
        aim -= int(value)

    elif direction == "down":
        aim += int(value)

print(horizontal*depth)