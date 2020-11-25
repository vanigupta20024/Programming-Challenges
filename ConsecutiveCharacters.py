'''
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
Return the power of the string.

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
'''

class Solution:
    def maxPower(self, s: str) -> int:
        current = 1
        max_freq = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                max_freq = max(current, max_freq)
                current = 1
        return max(max_freq, current)
