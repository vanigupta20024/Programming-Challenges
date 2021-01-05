'''
Count the number of prime numbers less than a non-negative number, n.
Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        l = [None for _ in range(n)]
        c = 0
        for i in range(2, n):
            if l[i] == None: c += 1
            j = 2
            while i * j < n:
                l[i * j] = True
                j += 1
        return c 
