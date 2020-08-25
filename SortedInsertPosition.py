# GHC Codepath - Module SE101
# Sandbox 10

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
# The function will be given a sorted array and a target 
# value, return the index if the target is found. If not, 
# return the index where it would be if it were inserted 
# in order.

def positionInsert(nums, target):
    if target in nums:
        return nums.index(target)
    elif target < nums[0]:
        return 0
    else:
        for i in range(1, len(nums)):
            if nums[i - 1] < target and nums[i] > target:
                return i
    return len(nums)
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = positionInsert(nums, target)

    fptr.write(str(result) + '\n')

    fptr.close()
