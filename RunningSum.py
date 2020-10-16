'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs = 0
        rs_num = []
        for i in nums:
            rs += i
            rs_num.append(rs)
        return rs_num
