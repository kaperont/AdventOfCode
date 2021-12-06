import csv
import numpy as np

def get_drawings():
    drawings = []

    with open("drawings.csv", newline='') as f:
        reader = csv.reader(f)
        drawings = list(reader)
        drawings = drawings[0]

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
            board.append(nums)
            i += 1
    
    return np.array(boards)

def play(drawings, boards):
    # Mark as found
    current = ''
    last_board = []
    board_loc = -1

    for drawing in drawings:
        current = drawing
        board_num = 0
        for board in boards:

            row_num = 0
            for row in board:

                val_num = 0
                for val in row:
                    if val == current:
                        boards[board_num][row_num][val_num] = ''
                    val_num += 1

                val_num = 0
                row_num +=1

            row_num = 0

            # Check for win!
            for row in board:
                row = boards[board_num][row_num]
                col = boards[board_num][:,row_num]

                if all(val == row[0] for val in row):
                    last_board = boards[board_num]
                    board_loc = board_num
                    boards = np.delete(boards, board_num, axis=0)
                    board_num -= 1
                    continue
                elif all(val == col[0] for val in col):
                    last_board = boards[board_num]
                    board_loc = board_num
                    boards = np.delete(boards, board_num, axis=0)
                    board_num -= 1
                    continue
                row_num += 1     

            board_num += 1

    print(len(boards), board_loc)

    return last_board, current



drawings = get_drawings()
boards = get_boards()

#print(boards[0][:,0])
winning_board, last = play(drawings,boards)

# Calculate score
sum = 0
for row in winning_board:
    for val in row:
        if val != '':
            sum += int(val)


print(sum, last)