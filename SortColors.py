'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of 
the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''

class Solution:
    def sortColors(self, a: List[int]) -> None:
        runner = 0
        left_partition = 0
        right_partition = len(a) - 1
        while runner <= right_partition:
            if a[runner] == 0:
                a[runner], a[left_partition] = a[left_partition], a[runner]
                runner += 1
                left_partition += 1
            elif a[runner] == 1:
                runner += 1
            else:
                a[runner], a[right_partition] = a[right_partition], a[runner]
                right_partition -= 1
        return a
