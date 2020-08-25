# GHC Codepath - Module SE101
# Sandbox 10

#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY nums as parameter.
# Implement bubble sort to sort nums and return the
# number of swaps it took to sort nums. 

def swap(num1, num2):
    num1, num2 = num2, num1

def bubble_sort(nums):
    last_index = len(nums) 
    swaps = 0
    while last_index > 0:
        for index in range(1, last_index):
            if nums[index] < nums[index - 1]:
                swap(nums[index], nums[index - 1])
                swaps += 1
        last_index -= 1
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    result = bubble_sort(nums)

    fptr.write(str(result) + '\n')

    fptr.close()
