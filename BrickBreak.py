# GHC Codepath SE101 
# Sandbox - 4
# BASIC

#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING bricks
#  2. INTEGER ball
# This function will check the string at the 
# index specified by the ball. If there is a
# brick ("-") in that index, it will be replaced
# with a space. Otherwise, nothing will be altered. 

def brickBreak(bricks, ball):
    string_ret = bricks[:ball]+" "+bricks[ball+1:]

    if bricks[ball] == "-":
        return(string_ret)
    return bricks
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bricks = input()

    ball = int(input().strip())

    result = brickBreak(bricks, ball)

    fptr.write(result + '\n')

    fptr.close()
