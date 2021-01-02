'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        c1, c2, c3 = 0, 1, 2
        while n > 2:
            c1, c2 = c2, c3
            c3 = c1 + c2
            n -= 1
        return c3
