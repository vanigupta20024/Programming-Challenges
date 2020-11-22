'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
'''

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        list1 = list2 = idx1 = idx2 = 0
        while list1 < len(word1) and list2 < len(word2):
            if word1[list1][idx1] == word2[list2][idx2]:
                idx1 += 1
                idx2 += 1
                if idx1 == len(word1[list1]):
                    idx1 = 0
                    list1 += 1
                if idx2 == len(word2[list2]):
                    idx2 = 0
                    list2 += 1
            else:
                return False
        return True
