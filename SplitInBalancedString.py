'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal_str = 0
        l = r = 0
        
        for i in range(len(s)):
            if s[i] == "L":
                l += 1
            else:
                r += 1
            if l == r:
                bal_str += 1
                l = r = 0
        return bal_str
