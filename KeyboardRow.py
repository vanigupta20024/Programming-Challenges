'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard.

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
'''

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        key1 = "qwertyuiop"
        key2 = "asdfghjkl"
        key3 = "zxcvbnm"
        result = []
        for word in words:
            var1 = var2 = var3 = 0
            for letter in word:
                if letter.lower() in key1: var1 += 1
                elif letter.lower() in key2: var2 += 1
                else: var3 += 1
            if var1 == len(word) or var2 == len(word) or var3 == len(word):
                result.append(word)
        return result
