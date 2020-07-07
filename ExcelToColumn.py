# GHC_Codepath 
# SE101
# Sandbox - 3

# Given a column as represented in excel, return
# its corresponding column number.
# Example:
# 
# A => 1
# B => 2
# C => 3
# ...
# Z => 26
# AA => 27
# AB => 28

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER.
# The function accepts STRING column as parameter. 

def excel_column_to_number(column):

    answer = 0
    # to keep current count of power of 26
    power = 1
    # looping in reverse order
    for i in range(len(column)-1, -1, -1):

        # to store alphas value between 1-26
        temp = ord(column[i]) - ord('A') + 1
        answer += temp*power
        power *= 26
        
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    column = input()

    result = excel_column_to_number(column)

    fptr.write(str(result) + '\n')

    fptr.close()
