'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        for index in range(len(nums)):
            val = nums[index]
            complement = target - val
            if complement in nums and nums.index(complement) != index:
                ret.append(nums.index(complement))
                ret.append(index)
                break
        return ret
