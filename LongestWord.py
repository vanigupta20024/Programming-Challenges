# GHC Codepath SE101 - Sandbox 3
# BASIC

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return a STRING.
# The function accepts STRING_ARRAY words as parameter.
# This function will go through an array of strings, 
# identify the largest word, and return that word. 

def longestWord(words):
    max_word = ""
    for i in words:
        # longest string on basis of len
        word = max(i.split(), key = len)
        
        if len(max_word) < len(word):
            max_word = word
            
    return max_word

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = longestWord(words)

    fptr.write(result + '\n')

    fptr.close()
