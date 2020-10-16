'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
'''

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if n >= len(nums):
            return nums
        
        ans = []
        temp = n
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[temp])
            temp += 1
        return ans
