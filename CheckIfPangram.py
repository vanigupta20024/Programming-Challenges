'''
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
 
Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        # naive approach - 1
        # freq = {}
        # for i in sentence:
        #     freq[i] = freq.get(i, 0) + 1
        # if len(freq) == 26: return True
        # return False
        
        # optimized approach - 2
        occurred = 0
        for i in sentence:
            temp = ord(i) - ord('a')
            occurred |= (1 << temp)
        if occurred == (1 << 26) - 1:
            return True
        return False
