#fishies = [4,3,3,5,4,1,2,1,3,1,1,1,1,1,2,4,1,3,3,1,1,1,1,2,3,1,1,1,4,1,1,2,1,2,2,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,5,1,4,2,1,1,2,1,3,1,1,2,2,1,1,1,1,1,1,1,1,1,1,4,1,3,2,2,3,1,1,1,4,1,1,1,1,5,1,1,1,5,1,1,3,1,1,2,4,1,1,3,2,4,1,1,1,1,1,5,5,1,1,1,1,1,1,4,1,1,1,3,2,1,1,5,1,1,1,1,1,1,1,5,4,1,5,1,3,4,1,1,1,1,2,1,2,1,1,1,2,2,1,2,3,5,1,1,1,1,3,5,1,1,1,2,1,1,4,1,1,5,1,4,1,2,1,3,1,5,1,4,3,1,3,2,1,1,1,2,2,1,1,1,1,4,5,1,1,1,1,1,3,1,3,4,1,1,4,1,1,3,1,3,1,1,4,5,4,3,2,5,1,1,1,1,1,1,2,1,5,2,5,3,1,1,1,1,1,3,1,1,1,1,5,1,2,1,2,1,1,1,1,2,1,1,1,1,1,1,1,3,3,1,1,5,1,3,5,5,1,1,1,2,1,2,1,5,1,1,1,1,2,1,1,1,2,1]

fishies = [8,7,6,5,4,3,2,1,0]

i=0
tock = 80
fish_per_day = {}
total = 0

def exponential_fish(t):
    """Returns the total number of fish on day t, starting with 1 new fish on day 0"""
    import numpy as np
    roots = np.roots((1, 0, 0, 0, 0, 0, 0,-1, 0,-1)) # roots of characteristic polynomial
    A = np.vstack([np.power(roots, n) for n in range(9)])
    coeff = np.linalg.solve(A, np.ones(9)) # coeff of solution to recurrence relation
    return int(coeff.dot(np.power(roots, t)).real.round())

exp = exponential_fish(80)
print(exp)
fish_per_day[8] = exp

for fish in fishies:
    small_fishies = []
    small_fishies.append(fish)

    if fish in fish_per_day:
        total += fish_per_day[fish]
    else:
        for tick in range(tock):
            for small_fish in small_fishies:
                if small_fish == 0:
                    small_fishies[i] = 7
                    small_fishies.append(9)
                small_fishies[i] -= 1
                i += 1
            i = 0
        fish_per_day[fish] = len(small_fishies)
        total += len(small_fishies)
        print(fish_per_day)
        print(total)

print('\n',fish_per_day)
print(total)
