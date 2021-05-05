'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 3: return True
        if len(s) == len(set(s)): return False
        
        def is_pal(s, l, h):
            if l < h:
                if s[l] == s[h]:
                    return is_pal(s, l + 1, h - 1)
                else:
                    return False
            return True
        
        l = 0
        h = len(s) - 1
        
        while l < h:
            if s[l] == s[h]:
                l += 1
                h -= 1
            else:
                if is_pal(s, l + 1, h) or is_pal(s, l, h - 1):
                    return True
                return False
        return True
