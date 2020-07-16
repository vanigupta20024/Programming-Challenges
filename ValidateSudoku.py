# GHC Codepath SE101
# Sandbox - 5
# Intermediate

# The function is expected to return a BOOLEAN.
# The function accepts 2D_STRING_ARRAY board as parameter.
# The function will analyze board, determine if it
# represents a valid sudoku board and returns true or
# false accordingly.

# rows: all unique numbers, blanks represented as "."
# columns: same as rows
# boxes: same as rows
# incomplete sudoku can be a valid sudoku if numbers are not repeating in row/column/boxes
# Example input:
# board = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return a BOOLEAN.
# The function accepts 2D_STRING_ARRAY board as parameter.
# The function will analyze board, determine if it
# represents a valid sudoku board and returns true or
# false accordingly.

def isValidSudoku(board):

    # check rows
    for i in range(len(board)):
        s = ""
        for j in range(len(board)):
            if board[i][j].isdigit():
                s += board[i][j]
        if len(s) != len(set(s)):
            return False
        
    # check columns
    for i in range(len(board)):
        s = ""
        for j in range(len(board)):
            if board[j][i].isdigit():
                s += board[j][i]
        if len(s) != len(set(s)):
            return False
        
    # boxes
    for i in range(0, 9, 3):
        s = ""
        for j in range(0, 9, 3):
            if board[i][j].isdigit():
                s += board[i][j]
        if len(s) != len(set(s)):
            return False

    return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    board_rows = int(input().strip())
    board_columns = int(input().strip())

    board = []

    for _ in range(board_rows):
        board.append(input().rstrip().split())

    result = isValidSudoku(board)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
