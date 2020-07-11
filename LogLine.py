# GHC Codepath SE101 
# Sandbox - 4
# BASIC

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY logs as parameter.
# Check the logs string array for errors and return
# the numbers of error messages. 
# Example:

# 5
# [WARNING] 403 Forbidden: No token in request parameters
# [ERROR] 500 Server Error: int is not subscriptable
# [INFO] 200 OK: Login Successful
# [INFO] 200 OK: User sent a message
# [ERROR] 500 Server Error: int is not subscriptable

# should return 3 as loglines with value 200 or less are not errors

def countErrors(logs):

    count = 0
    for i in logs: 
        # method 1
        ans = ''.join(val for val in i if val.isdigit())
        if int(ans) > 200:
            count += 1

        # method 2
        # l = i.split() 
        # ans = filter(str.isdigit, l)
        # for i in ans:
        #     if int(i) > 200:
        #         count += 1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    result = countErrors(logs)

    fptr.write(str(result) + '\n')

    fptr.close()
