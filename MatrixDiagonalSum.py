'''
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        i = j = k = 0
        l = len(mat) - 1
        
        mat_sum = 0
        while i < len(mat):
            mat_sum += mat[i][j] + mat[k][l]
            
            if i == k and j == l:
                mat_sum -= mat[i][j]
            
            i += 1
            j += 1
            k += 1
            l -= 1
            
        return mat_sum
