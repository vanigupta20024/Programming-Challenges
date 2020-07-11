# GHC Codepath SE101
# BASIC
# Sandbox - 4

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER.
# The function accepts STRING vals as parameter.
# The function will summate the ASCII values of
# the characters in the string it accepts as a
# parameter. 

def summate(vals):

    sum_string = 0 
    
    # assumption: all elements in a string are letters
    for i in vals:
        sum_string += ord(i)
        
    return sum_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    vals = input()

    result = summate(vals)

    fptr.write(str(result) + '\n')

    fptr.close()
