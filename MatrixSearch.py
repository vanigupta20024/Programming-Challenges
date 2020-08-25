# GHC Codepath - SE101
# Sandbox 10

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY A
#  2. INTEGER B
# The function will search for B inside A. Return 1 
# if B is found and 0 if B is not found. 

def binary_row(a, b):
    low = 0
    high = len(a) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == b:
            return mid
        if a[mid] < b:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def search(a, b):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if b >= a[mid][0] and b <= a[mid][len(a) - 1]:
            if binary_row(a[mid], b) != -1:
                return 1
        elif b >= a[mid][0]:
            low = mid + 1
        elif b < a[mid][0]:
            high = mid - 1
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    A_rows = int(input().strip())
    A_columns = int(input().strip())

    A = []

    for _ in range(A_rows):
        A.append(list(map(int, input().rstrip().split())))

    B = int(input().strip())

    result = search(A, B)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
