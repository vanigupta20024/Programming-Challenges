'''
You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column 
number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = [[1,2], [3,4]]
r = 1, c = 4
Output:  [[1,2,3,4]]

Example 2:
Input: 
nums =  [[1,2], [3,4]]
r = 2, c = 4
Output:  [[1,2], [3,4]]
'''

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        num_of_rows = len(nums)
        num_of_columns = len(nums[0])
        
        if num_of_rows * num_of_columns != r * c:
            return nums
        
        matrix = []
        row = col = 0
        for row_index in range(r):
            temp = []
            for col_index in range(c):
                if col >= num_of_columns:
                    col = 0
                    row += 1
                num = nums[row][col]
                col += 1
                temp.append(num)
            matrix.append(temp)
        return matrix
