# GHC Codepath SE101
# Sandbox - 5
# Basic 

# input of the form: 
[(0,0), (0,2), (1,1), (1,2), (2,2)] # Player 1 wins (diagonal)
[(0,0), (0,2), (1,0), (2,0), (2,2), (1,1)] # player 2 wins (diagonal)

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY board as parameter.
# The function accepts a 2D array of ints representing
# moves made by the players. Return 1 if player 1 wins,
# 2, if player 2 wins, and -1 if no one wins. 

def check(a):
    # rows
    for i in range(len(a)):
        if a[i][0] == a[i][1] == a[i][2]:
            return a[i][0]
    # columns
    for i in range(len(a)):
        if a[0][i] == a[1][i] == a[2][i]:
            return a[0][i]

    # main diagnomal
    if a[0][0] == a[1][1] == a[2][2]:
        return a[0][0]

    # other diagonal
    if a[2][0] == a[1][1] == a[0][2]:
        return a[2][0]
    return -1


def tictactoe(board):
    a = [[-1 for i in range(3)] for j in range(3)]
    for i in range(len(board)):
        x = board[i][0]
        y = board[i][1]
        if i % 2 == 0:
            a[x][y] = 1
        else:
            a[x][y] = 2

    return check(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    board_rows = int(input().strip())
    board_columns = int(input().strip())

    board = []

    for _ in range(board_rows):
        board.append(list(map(int, input().rstrip().split())))

    result = tictactoe(board)

    fptr.write(str(result) + '\n')

    fptr.close()
