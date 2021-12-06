input = open("input_two.txt", "r").readlines()
measurements = [int(row) for row in input]

total = 0
previous = 0

for i in range(len(measurements)):
    next_three = measurements[i:i+3]

    print(next_three)
    tsum = sum(next_three)
    print(tsum)

    if i != 0 and tsum > previous:
        total += 1

    previous = tsum

print(total)