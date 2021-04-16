'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if len(word) < 2:
            return True
        
        lower = upper = 0
        
        for letter in word:
            if letter.isupper(): upper += 1
            else: lower += 1
        
        if (upper == 0) or (lower == 0) or (upper == 1 and word[0].isupper()):
            return True
        return False
