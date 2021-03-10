'''
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
'''

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i in hashmap.keys():
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        sum = 0
        for k, v in hashmap.items():
            if v == 1: sum += k
        return sum
