'''
Given a binary array, find the maximum number of consecutive 1s in this array.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # nums = [str(i) for i in nums]
        # return max(map(len, ("".join(nums).split("0"))))
        
        mx = 0
        mx2 = 0
        for i in nums:
            if i == 1:
                mx2 += 1
            else:
                if mx < mx2: 
                    mx = mx2
                mx2 = 0
            if mx < mx2: mx = mx2
        return mx
