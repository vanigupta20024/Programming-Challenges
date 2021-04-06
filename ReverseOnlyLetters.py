'''
Given a string S, return the "reversed" string where all characters that 
are not a letter stay in the same place, and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
'''

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = []
        s = ""
        for i in range(len(S)):
            if S[i].isalpha(): stack.append(S[i])
        for i in S:
            if not i.isalpha(): s += i
            else: s += stack.pop()
        return s
