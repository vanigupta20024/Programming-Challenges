'''
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
'''

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) == len(set(nums)):
            return 0
        frequency = {}
        for index in nums:
            if index in frequency.keys():
                frequency[index] += 1
            else:
                frequency[index] = 1
        answer = 0
        for key, val in frequency.items():
            answer += (val*(val - 1)) // 2
        return answer
