# GHC_Codepath 
# Sandbox - 3
# SE101: Is Valid Sentece?

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return a BOOLEAN.
# The function accepts STRING sentence as parameter.
# The function will check if the sentence is valid 
# and return true or false accordingly. 

def isValid(sentence):

    # sentence can end with any of the three punctuations
    # an endswith function can take multiple arguments using a tuple
    if sentence[0].isupper() and sentence.endswith((".","!","?")): return True
    else: return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = isValid(sentence)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
