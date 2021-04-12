'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            while (left < right) and not (s[left].isdigit() or s[left].isalpha()):
                left += 1
            while (left < right) and not (s[right].isdigit() or s[right].isalpha()):
                right -= 1
            if s[left].isdigit() and s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
