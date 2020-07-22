# Codepath SE101 
# Sandbox - 6 
# BASIC

#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER.
# The function accepts STRING text as parameter.
# Given a string representing some text, count
# how many time each unique letter appears in the
# given string. 

def countLetters(text):

    d = {}
    for i in text:
        if i.isalpha():
            d[i.upper()] = d.get(i.upper(), 0) + 1
        else:
            d[i] = d.get(i, 0) + 1

    st = ""
    for k, v in d.items():
        st += k + str(v) + "\n"

    return st[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text = input()

    result = countLetters(text)

    fptr.write(str(result) + '\n')

    fptr.close()
