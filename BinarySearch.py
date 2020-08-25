# GHC Codepath - Module SE101
# Sandbox - 10

#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
# This function will search for target in nums. 
# If target exists, then return its index, otherwise 
# return -1.

def search(nums, target):
    low = 0
    high = len(nums) - 1

    while (high - low) > 1:

        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid
        elif nums[mid] > target:
            high = mid

    return -1

# def search(nums, target, low, high):
#     if high - low == 1:
#         return -1
#
#     mid = (low + high) // 2
#     if nums[mid] == target:
#         return mid
#     if nums[mid] < target:
#         return search(nums, target, mid, high)
#     else:
#         return search(nums, target, low, mid)

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = search(nums, target)

    fptr.write(str(result) + '\n')

    fptr.close()
