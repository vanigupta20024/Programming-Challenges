# GHC Codepath SE101
# Sandbox - 4
# BASIC

#!/bin/python3

import math
import os
import random
import re
import sys



# The function is expected to return a BOOLEAN.
# The function accepts STRING_ARRAY words as parameter.
# Check if each word in words starts with the same 
# letter and return true or false accordingly. 

def isAlliteration(words):
    for i in range(len(words)-1):
        if words[i][0] != words[i+1][0]:
            return False
    return True

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = isAlliteration(words)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
