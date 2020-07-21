# Project Euler - Problem 10
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time
start = time.time()

n = 2000000
def isprime(n):
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return 0
	return 1

s = 2
for i in range(2, n):
	if i % 2 != 0 and isprime(i):
		s += i

print(s)
print(time.time() - start, "sec")
