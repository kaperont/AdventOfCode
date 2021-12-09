fish_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
with open('input.txt') as f:
    for fish in f.read().split(','):
        fish_counts[int(fish.strip())] += 1

for i in range(256):
    fish_counts.append(fish_counts.pop(0))
    fish_counts[6] += fish_counts[8]

print(sum(fish_counts))