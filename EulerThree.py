# Project Euler - Problem 3
# What is the largest prime factor of the number 600851475143 ?

import time
start = time.time()

n = 600851475143 
i = 2
x = 0
while n > 1:
	if n % i == 0:
		while n % i == 0:
			n /= i
			x = i
	i += 1

print(x)
print(time.time() - start, "sec")
