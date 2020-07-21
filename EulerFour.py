# Project Euler - Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.

import time
start = time.time()

def pal(s):
	i = 0
	j = len(s) - 1
	while i < j:
		if s[i] != s[j]:
			return 0
		i += 1
		j -= 1
	return 1

n1 = 100
n2 = 1000 # exclusive
mx = 0
for i in range(n1, n2):
	for j in range(n1, n2):
		if pal(str(i * j)) and mx < i * j:
			mx = i * j

print(mx)
print(time.time() - start, "sec")
