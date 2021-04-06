'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater 
than or equal to k characters, then reverse the first k characters and left the other as original. 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
'''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        if k >= len(s):
            return s[::-1]
        
        i = 0
        s = list(s)
        while i < len(s):
            l = i
            h = (i + k - 1) if (i + k - 1) < len(s) else len(s) - 1
            while l < len(s) and l < h:
                s[l], s[h] = s[h], s[l]
                l += 1
                h -= 1
            i += (2 * k)
        return "".join(s)
