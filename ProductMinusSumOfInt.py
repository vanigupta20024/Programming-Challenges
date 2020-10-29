'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''

from functools import reduce
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = [int(i) for i in str(n)]
        pro = reduce((lambda x,y: x*y), n)
        summ = reduce((lambda x,y: x+y), n)
        return pro - summ
