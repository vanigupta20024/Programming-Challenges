# GHC Codepath SE101 
# Sandbox - 6
# Hard
'''
Input: 
I do not like green eggs and ham,
I do not like them, Sam-I-Am!
I do not like them with a fox,
I do not like them in a box.
I do not like them here or there,
I do not like them anywhere!
I do not like them, Sam-I-Am,
I do not like green eggs and ham!

Output:
I do : not (8) 
do not : like (8) 
not like : green (2) 
them, (2) 
them (4) 
like green : eggs (2) 
green eggs : and (2) 
eggs and : ham, (1) 
ham! (1) 
and ham, : I (1) 
ham, I : do (1) 
like them, : Sam-I-Am! (1) 
Sam-I-Am, (1) 
them, Sam-I-Am! : I (1) 
Sam-I-Am! I : do (1) 
like them : with (1) 
in (1) here (1) 
anywhere! (1) 
them with : a (1) 
with a : fox, (1) 
a fox, : I (1) 
fox, I : do (1) 
them in : a (1) 
in a : box. (1) 
a box. : I (1) 
box. I : do (1) 
them here : or (1) 
here or : there, (1) 
or there, : I (1) 
there, I : do (1) 
them anywhere! : I (1) 
anywhere! I : do (1) 
them, Sam-I-Am, : I (1) 
Sam-I-Am, I : do (1)
'''

#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return a STRING.
# The function accepts STRING text as parameter.
# The function will break the text into individual 
# words. For every two words, the frequency of words 
# that come after these two words will be counted and 
# returned as a string.

def bigram_frequency_analyzer(text):
    l = text.split()
    d = {}
    phrase = ""
    for i in range(0, len(l) - 2):
        k = " ".join(l[i:i+2])
        if k in d.keys():
            if l[i + 2] in d[k].keys():
                d[k][l[i + 2]] += 1
            else:
                d[k][l[i + 2]] = 1
        else:
            d[k] = {l[i + 2] : 1}

    for k, v in d.items():
        phrase += k + " : "
        for k1, v1 in d[k].items():
            phrase += k1 + " (" + str(v1) + ") "
        phrase += "\n"
    return phrase.strip()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text = input()

    result = bigram_frequency_analyzer(text)

    fptr.write(result + '\n')

    fptr.close()
