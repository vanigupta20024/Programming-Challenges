'''
You are given a string s that consists of lower case English letters and brackets. 
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"

Example 4:
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
'''

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            while i < len(s) and s[i] != ")":
                stack.append(s[i])
                i += 1
            temp = ""
            if i < len(s) and s[i] == ")":
                while stack[-1] != "(":
                    temp += stack.pop()
                i += 1
                stack.pop()
            if temp != "":
                for letter in temp:
                    stack.append(letter)
        return "".join(stack)
            
