'''
Input Format

The first line contains a single integer, n, denoting the number of strings.
Each line i of the n subsequent lines consists of a single string,s, denoting a sequence of brackets.
'''

#!/bin/python3

import math
import os
import random
import re
import sys


def braces(values):
    ans = []
    for index in values:
        stack = []
        flag = 0
        for i in index:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if i == ")":
                    if len(stack) != 0 and stack[-1] == "(":
                        stack.pop()
                    else: 
                        ans.append("NO")
                        flag = 1
                        break
                elif i == "}":
                    if len(stack) != 0 and stack[-1] == "{":
                        stack.pop()
                    else: 
                        ans.append("NO")
                        flag = 1
                        break
                elif i == "]":
                    if len(stack) != 0 and stack[-1] == "[":
                        stack.pop()
                    else:
                        ans.append("NO")
                        flag = 1
                        break
                else:
                    ans.append("NO")
                    flag = 1
                    break
        if len(stack) == 0 and flag != 1:
            ans.append("YES")
        else:
            if flag == 0:
                ans.append("NO")
    return ans

if __name__ == '__main__':
    t = int(input())
    x = []
    for t_itr in range(t):
        expression = input()
        x.append(expression)
    ans = braces(x)
    ans = "\n".join(ans)
    print(ans)
