input = open("input.txt", "r").readlines()

totals = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for line in input:

    i = 0
    for c in line:
        if c == '\n':
            continue
        if int(c) == 0:
            totals[0][i] += 1
        elif int(c) == 1:
            totals[1][i] += 1
        i+=1

final = []
ep_final = []
for i in range(12):
    if totals[0][i] > totals[1][i]:
        final.append(0)
    else:
        final.append(1)

print(final)

gamma_rate = ''.join(str(bin) for bin in final)

for i in final:
    if final[i] == 1:
        ep_final.append(1)
    elif final[i] == 0  :
        ep_final.append(0)

print(ep_final)

epsilon_rate = ''.join(str(bin) for bin in ep_final)

print(int(gamma_rate,2)*int(epsilon_rate,2))