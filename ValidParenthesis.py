'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_dic = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        for i in s:
            if i == "{" or i == "[" or i == "(":
                stack.append(i)
            else:
                if len(stack) > 0 and stack[-1] == par_dic[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0: return True
        return False
