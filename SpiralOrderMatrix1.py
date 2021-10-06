'''
Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.
'''

class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, A):
        top = 0
        bottom = len(A)
        left = 0
        right = len(A[0])
        dir = 'r'
        answer = []
        while top < bottom and left < right:
            if dir == 'r':
                for i in range(left, right):
                    answer.append(A[top][i])
                top += 1
                dir = 'd'
            elif dir == 'd':
                for i in range(top, bottom):
                    answer.append(A[i][right - 1])
                right -= 1
                dir = 'l'
            elif dir == 'l':
                for i in range(right - 1, left - 1, -1):
                    answer.append(A[bottom - 1][i])
                bottom -= 1
                dir = 'u'
            elif dir == 'u':
                for i in range(bottom - 1, top - 1, -1):
                    answer.append(A[i][left])
                left += 1
                dir = 'r'
        return answer
