# GHC_Codepath
# Sandbox - 3
# 1. SE101:String to Integer (ATOI) 

# Implement atoi which converts a string to an integer. 

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, 
# takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value. 
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function. 
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains 
# only whitespace characters, no conversion is performed. If no valid conversion could be performed, a zero value is returned. 

# Note: 
# • Only the space character' is considered as whitespace character. 
# • Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [-231. 231 - 1]. If the numerical value is out of the range of representable values, INT_MAX (231 - 1) or INT_MIN (-231) is returned. 

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER.
# The function accepts STRING a as parameter.
# The function will convert the string parameter 
# into an integer, and return the result. 


def atoi(a):

    # strip whitespaces from input
    a = a.strip()

    # if starting character is a letter
    # return zero, as mentioned
    if a[0].isalpha(): return 0

    # to store the sign of number
    sign = 0
    if a.startswith("-"): sign = 1

    # to index upto a digit
    i = 0
    while i < len(a) and not a[i].isdigit():
        i += 1

    # to take all digits until a space/alpha is found
    ans = 0
    while i < len(a) and a[i].isdigit():
        ans = ans*10 + int(a[i])
        i += 1

    # replacing back the sign
    if sign == 1:
        ans = -ans
    
    # following the boundary checks 
    if ans < -(2**31): return -2**31
    if ans > 2**31 - 1: return 2**31 - 1
    return ans
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    result = atoi(a)

    fptr.write(str(result) + '\n')

    fptr.close()
