# Project Euler - Problem 7
# What is the 10 001st prime number?

import time
start = time.time()

def isprime(n):
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return 0
	return 1

n = 10001
c = 1
x = 2
while c < n + 1:
	if isprime(x):
		c += 1
	x += 1

print(x - 1)
print(time.time() - start, "sec")
