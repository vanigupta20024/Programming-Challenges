# GHC Codepath Sandbox - 6
# BASIC

#!/bin/python3

import math
import os
import random
import re
import sys

'''
"(255,0,0)(255,0,0)(255,0,0)(0,255,0)(0,255,0)(0,255,0)(0,0,255)(0,0,255)(0,0,255)" 

with an image of size 3, should return:

"3x(255,0,0)3(0,255,0)3(0,0,255)3"
'''

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING colors
#  2. INTEGER size

def countColors(colors, size):
    s = str(size) + "x"
    d = {}
    l = colors.replace("(", "").replace(")", " ").split()

    for i in l:
        d[i] = d.get(i, 0) + 1
    
    for k, v in d.items():
        s += "(" + k + ")" + str(v)

    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    colors = input()

    size = int(input().strip())

    result = countColors(colors, size)

    fptr.write(result + '\n')

    fptr.close()
