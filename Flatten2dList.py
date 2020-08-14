# GHC Codepath - Sandbox 9
# Basic

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# output: [1,2,3,4,5,6,7,8,9]

l = []
def flatten_array(matrix):
    return ",".join(flat(matrix, 0, 0))

def flat(matrix, row, col):
    l.append(str(matrix[row][col]))
    if col == len(matrix[row]) - 1:
        if row == len(matrix) - 1:
            return l
        return flat(matrix, row + 1, 0)
    return flat(matrix, row, col + 1)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    matrix_rows = int(input().strip())
    matrix_columns = int(input().strip())

    matrix = []

    for _ in range(matrix_rows):
        matrix.append(list(map(int, input().rstrip().split())))

    result = flatten_array(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
