# Project Euler - Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time
start = time.time()

for i in range(2, 1000):
	for j in range(i + 1, 1000):
		if i + j >= 1000:
			break
		k = 1000 - i - j
		if i**2 + j**2 == k**2:
			print(i * j * k)
			break

print(time.time() - start, "sec")
