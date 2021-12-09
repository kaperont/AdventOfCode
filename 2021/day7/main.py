import csv

def get_horizontals():
    horizontals = []

    with open("input.csv", newline='') as f:
        reader = csv.reader(f)
        horizontals = list(reader)
        horizontals = horizontals[0]

        horizontals = [int(num) for num in horizontals]

    return horizontals

horizontals = get_horizontals()
avg = (sum(horizontals) / len(horizontals))

least = 100000000000000000000
for i in range(200, 1500):
    fuel_points = 0

    for num in horizontals:
        fuel_plus = 1
        if num < i:
            while num != i:
                fuel_points += fuel_plus
                fuel_plus += 1
                num += 1
        elif num > i:
            while num != i:
                fuel_points += fuel_plus
                fuel_plus += 1
                num -= 1
    if fuel_points < least:
        least = fuel_points
        print(least)

print(least)