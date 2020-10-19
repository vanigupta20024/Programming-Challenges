'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
'''

class Solution:
    def toLowerCase(self, s: str) -> str:
        for index in range(len(s)):
            if ord(s[index]) < ord('a') and s[index].isalpha():
                x = ord(s[index]) - ord('A') + ord('a')
                s = s[: index] + chr(x) + s[index + 1:]
        return s
