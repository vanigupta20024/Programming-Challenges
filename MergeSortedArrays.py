# GHC Codepath - Module SE101
# Sandbox - 10

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums1
#  2. INTEGER_ARRAY nums2
#  3. INTEGER m
#  4. INTEGER n
# This function will merge nums1 and nums2 into 1
# sorted array. m and n indicated how many elements
# are initialized in nums1 and nums2 respectively.

def merge(nums1, nums2, m, n):
    pointer_nums1 = 0
    pointer_nums2 = 0

    while pointer_nums2 < n:
        if pointer_nums1 == len(nums1):
            nums1 += nums2
            break
        if nums2[pointer_nums2] <= nums1[pointer_nums1] or nums1[pointer_nums1] == 0:
            nums1.insert(pointer_nums1, nums2[pointer_nums2])
            pointer_nums2 += 1
            pointer_nums1 += 1
        else:
            pointer_nums1 += 1

    return nums1[:m + n]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums1_count = int(input().strip())

    nums1 = []

    for _ in range(nums1_count):
        nums1_item = int(input().strip())
        nums1.append(nums1_item)

    nums2_count = int(input().strip())

    nums2 = []

    for _ in range(nums2_count):
        nums2_item = int(input().strip())
        nums2.append(nums2_item)

    m = int(input().strip())

    n = int(input().strip())

    result = merge(nums1, nums2, m, n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
