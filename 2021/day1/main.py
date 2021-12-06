input = open("input.txt", "r").readlines()

total = 0
previous = int(input[0])

for num in input:
    if int(num) > previous:
        total += 1

    previous = int(num)

print(total)