'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        
        # create a hash map
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        if len(set(dic.values())) != len(set(arr)):
            return False
        return True
