input = open("input.txt", "r").readlines()

codes = []

for line in input:
    lr = line.split(" | ")
    left = lr[0].split()
    right = lr[1].split()

    codes.append([left, right])

# for code in codes:
#     print(code)

total = 0
i=0
codebook = {}
one = ''
for code in codes:
    for input in code:
        if len(input) == 2:
            codebook[input] = 1
            one = input
        elif len(input) == 3:
            codebook[input] = 7
        elif len(input) == 4:
            codebook[input] = 4
        elif len(input) == 7:
            codebook[input] = 8
        
print(total)