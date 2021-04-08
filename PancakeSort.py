# GHC Codepath 
# Module SE101
# Sandbox 10

# Sample input:
# [1,2,3]
# Output: []
# Explaination: The input is already sorted, so there is no need to flip anything.
# Note that other answers, such as [3, 3], would also be accepted.

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY A as parameter.
# The function will implement the pancake sorting 
# algorithm to reverse the order of the first k (where
# k <= A.length). Return the k values corresponding to 
# a sequence of pancake flips that sort A.

def flip(arr):
    return arr[::-1]

def pancakeSort(a):
    
    end_of_list = len(a) - 1
    flip_list = []
    while end_of_list > 0:
        max_element = max(a[:end_of_list + 1])
        index_max_element = a.index(max_element)
        if index_max_element != end_of_list:
            a = flip(a[:index_max_element + 1]) + a[index_max_element + 1:]
            flip_list.append(index_max_element + 1)
            a = flip(a[:end_of_list + 1]) + a[end_of_list + 1:]
            flip_list.append(end_of_list + 1)
        end_of_list -= 1
    return flip_list
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    A_count = int(input().strip())

    A = []

    for _ in range(A_count):
        A_item = int(input().strip())
        A.append(A_item)

    result = pancakeSort(A)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
