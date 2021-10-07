'''
You are in an infinite 2D grid where you can move in any of the 8 directions

 (x,y) to 
    (x-1, y-1), 
    (x-1, y)  , 
    (x-1, y+1), 
    (x  , y-1),
    (x  , y+1), 
    (x+1, y-1), 
    (x+1, y)  , 
    (x+1, y+1) 
You are given a sequence of points and the order in which you need to cover the points.. 
Give the minimum number of steps in which you can achieve it. You start from the first point.

Input 1:

 A = [0, 1, 1]
 B = [0, 1, 2]

Output 1:
2

Explanation 1:
Given three points are: (0, 0), (1, 1) and (1, 2).
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
'''
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def coverPoints(self, A, B):
        steps = 0
        for i in range(1, len(A)):
            x0 = A[i - 1]
            y0 = B[i - 1]
            x1 = A[i]
            y1 = B[i]
            steps += max(abs(x0 - x1), abs(y0 - y1))
        return steps
