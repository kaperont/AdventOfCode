import csv

def get_drawings():
    drawings = []

    with open("drawings.csv", newline='') as f:
        reader = csv.reader(f)
        drawings = list(reader)
        drawings = drawings[0]
        drawings = [int(drawing) for drawing in drawings]

    return drawings

def get_boards():
    board_input = open("boards.txt", "r").readlines()

    boards = []
    board = []
    i=0
    for line in board_input:
        if i == 5:
            boards.append(board)
            board = []
            i = 0
            continue
        else:
            nums = line.split()
            nums = [int(num) for num in nums]
            board.append(nums)
            i += 1
    
    return boards

random_numbers = get_drawings()
grids = get_boards()
print(random_numbers)

memo = {}
for num in random_numbers:
    memo[num] = []
for gi, grid in enumerate(grids):
    for ri, row in enumerate(grid):
        for ci, num in enumerate(row):
            if num in memo:
                memo[num].append((gi, ri, ci))
                
def is_win(grid, row, col):
    grid[row][col] = -1
    if sum(grid[row]) == -5:
        return True
    if sum([row[col] for row in grid]) == -5:
        return True
    return False

winners = []
def process_winner(grids, grid_indexes):
    # Loop through all given grid indexes
    for gi, ri, ci in grid_indexes:
        # Ignore if already processed
        if gi in winners:
            continue

        # Get grid
        grid = grids[gi]
        if is_win(grid, ri, ci):
            winners.append(gi)

            # if all the winners are found, 
            # return the sum of unmarked numbers and multiply by the random number.
            if len(winners) == len(grids):
                return sum(
                    [(0 if grid[i][j] == -1 else grid[i][j]) for i in range(5) for j in range(5)]
                ) * num
    return None

ans = None
# Loop through all random numbers
for num in random_numbers:
    ans = process_winner(grids, memo[num])
    # If all the winners are found, break
    if ans is not None:
        break
print(f'Answer: {ans}')