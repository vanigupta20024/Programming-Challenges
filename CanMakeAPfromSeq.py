'''
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.
Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
'''

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        s = sorted(arr)
        diff = s[0] - s[1]
        for i in range(2, len(s)):
            if diff != s[i - 1] - s[i]:
                return False
        return True
