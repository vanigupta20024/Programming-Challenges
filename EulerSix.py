# Project Euler - Problem 6
# Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.

import time
start = time.time()

n = 100
f1 = (n * (n + 1) * (2 * n + 1))//6
f2 = (n *(n + 1))//2

print(f2**2 - f1)
print(time.time() - start, "sec")
