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
    for drawing in drawings:
        current = drawing
        board_num = 0
        new_boards = boards
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
                row = new_boards[board_num][row_num]
                col = new_boards[board_num][:,row_num]

                if all(val == row[0] for val in row):
                    last_board = boards[board_num]
                    new_boards = np.delete(boards, board_num, axis=0)
                    boards = new_boards
                    print(last_board, board_num)
                    board_num -= 1
                    continue
                elif all(val == col[0] for val in col):
                    last_board = boards[board_num]
                    new_boards = np.delete(boards, board_num, axis=0)
                    boards = new_boards
                    print(last_board, board_num)
                    board_num -= 1
                    continue
                row_num += 1     

            board_num += 1

    print(boards, len(boards), current)
    return boards, current




drawings = get_drawings()
boards = get_boards()

#print(boards[0][:,0])
won=0
winning_board = []
winning_board, last = play(drawings, boards)
# while won == 0:
#     won, board, loc, last = play(drawings,boards)
#     if won == 0:
#         winning_board = board
#         boards = np.delete(boards, loc, axis=0)
#     elif won == 1:
#         print(winning_board)
#         break


print(winning_board)


# Calculate score
sum = 0
for row in winning_board:
    for val in row:
        if val != '':
            sum += int(val)


print(int(sum)*int(last))

print(winning_board, last)