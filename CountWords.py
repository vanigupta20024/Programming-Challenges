# GHC Codepath Sandbox - 6
# Module SE101
# BASIC

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return a STRING.
# The function accepts STRING text as parameter.
# The function will analyze the words in text
# and count how many times each word appears. The
# words with their corresponding counts will be returned. 

def count_words(text):
    l = text.replace(",","").replace(".","").split()
    d = {}
    for i in l:
        d[i.lower()] = d.get(i.lower(), 0) + 1

    s = "".join([i + " " + str(j) + "\n" for i,j in d.items()])
    return s[: -1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text = input()

    result = count_words(text)

    fptr.write(result + '\n')

    fptr.close()
