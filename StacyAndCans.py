'''
Cans are lined up in a single row, and Stacey indexes them from 0 to n-1, starting from the first can to the nth can in line. 
In each selection, she picks the lightest remaining can on the beach with weight w, and uses the scooper to pick up that 
can along with the two cans adjacent to it. She repeats this process until there are no more cans left on the beach. Stacey 
wants to find the sum of the weights of the lightest cans which she chooses in every selection. 

Note: If there are two cans with the lightest weight at different indexes, Stacey chooses the can at the smallest index. 
If the can only has one other can adjacent to it, then the can itself and the single adjacent can will be removed. 

Example 
Let there be n = 4 cans on the beach with weights represented by weights = (4, 3, 2, 1]. 
First, choose the minimum weight (i.e. 1) and add that weight up to the total. The cans with weights 2 and 1 are removed. 
The array of cans is now [4, 3]. • Then, choose the minimum weight from the remaining cans (i.e. 3) and add that weight up to the total. 
The cans with weights 3 and 4 are removed, and now there are no more cans on the beach. 
Hence, the total is 1 + 3 = 4. 

'''

import math
import os
import random
import re
import sys


def findTotalWeight(cans):
    sum_of_cans = 0
    while len(cans):
        minimum = min(cans)
        i = cans.index(minimum)
        sum_of_cans += cans[i]
        if i < len(cans) - 1 and i > 0:
            cans = cans[: i - 1] + cans[i + 2:]
        else:
            if i == 0:
                cans = cans[2:]
            elif i == len(cans) - 1:
                cans = cans[:len(cans) - 2]
    return sum_of_cans
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cans_count = int(input().strip())

    cans = []

    for _ in range(cans_count):
        cans_item = int(input().strip())
        cans.append(cans_item)

    result = findTotalWeight(cans)

    fptr.write(str(result) + '\n')

    fptr.close()
