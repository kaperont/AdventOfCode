input = open("input.txt", "r").readlines()

oxygen_list = []
co2_list = []

totals = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

i=0
ones = 0
zeros = 0

for line in input:

    oxygen_list.append(line)
    co2_list.append(line)

    i = 0
    for c in line:
        if c == '\n':
            continue
        if int(c) == 0:
            totals[0][i] += 1
        elif int(c) == 1:
            totals[1][i] += 1
        i+=1

print(totals)

def ox(oxygen_list):
    i=0
    for j in range(12):

        if len(oxygen_list) == 1:
            oxygen_list[0] = oxygen_list[0].rstrip('\n')
            print(oxygen_list)
            return oxygen_list

        elif totals[0][i] > totals[1][i]:
            oxygen_list = [num for num in oxygen_list if num[j] == '0']

        else:
            oxygen_list = [num for num in oxygen_list if num[j] == '1']

        i+=1

def co2(co2_list):
    i=0
    for j in range(12):

        if len(co2_list) == 1:
            co2_list[0] = co2_list[0].rstrip('\n')
            print(co2_list)
            return co2_list

        elif totals[0][i] > totals[1][i]:
            co2_list = [num for num in co2_list if num[j] == '1']
            
        else:
            co2_list = [num for num in co2_list if num[j] == '0']

        i+=1
        print("CO2 LIST\n\n", co2_list)

oxygen_list = ox(oxygen_list)
co2_list = co2(co2_list)

print(int(oxygen_list[0],2)*int(co2_list[0],2))