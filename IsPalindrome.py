# GHC_Codepath
# SE101: Is Palindrome?

#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER.
# The function accepts STRING a as parameter.
# Check if a is a palindrome and return 1 if it
# is a palindrome and 0 if it is not. 

def isPalindrome(a):

    # since input contains spaces and non alphanumeric
    # characters, we need to check that as well

    # since original string can have non-alpha
    # characters and upper case alpha too
    new_string = ""
    for i in range(len(a)):
        if a[i].isalpha():
            new_string += a[i].lower()
    # i = 0
    # j = len(new_string) - 1
    # while i < j:
    #     if new_string[i] !=new_string[j]:
    #         return 0
    #     i += 1
    #     j -= 1
    # return 1
    # another way:
    if new_string == new_string[::-1]:
            return 1
    else: return 0
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    result = isPalindrome(a)

    fptr.write(str(result) + '\n')

    fptr.close()
