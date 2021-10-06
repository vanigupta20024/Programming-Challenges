'''
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A. The sub-array should be contiguous 
i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid. Maximum sub-array is 
defined in terms of the sum of the elements in the sub-array. Find and return the required subarray.

NOTE:  

If there is a tie, then compare with segment's length and return segment which has maximum length.
If there is still a tie, then return the segment with minimum starting index.

Example Input
Input 1:
A = [1, 2, 5, -7, 2, 3]
Input 2:
A = [10, -1, 2, 3, -4, 100]
Example Output
Output 1:
[1, 2, 5]
Output 2:
[100]
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, a):
        max_sum = []
        m_start = -1
        for i in range(len(a)):
            l = [a[i]]
            l_start = i
            for j in range(i + 1, len(a)):
                if a[j] >= 0:
                    l.append(a[j])
                else:
                    break
            if sum(l) > sum(max_sum):
                max_sum = l
                m_start = l_start
            elif sum(l) == sum(max_sum):
                if len(l) > len(max_sum):
                    max_sum = l
                if l_start < m_start:
                    max_sum = l
        return max_sum
