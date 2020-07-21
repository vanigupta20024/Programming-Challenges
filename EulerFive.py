# Project Euler - Problem 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Method 1: Exec time: 0.0004 secs
import time
start = time.time()

d = {i: 0 for i in range(2, 11)}
for i in range(2, 11):
	for j in range(2, i+1):
		c = 0
		if i % j == 0:
			while i % j == 0:
				i /= j
				c += 1
		if d[j] < c:
			d[j] = c
p = 1
for k, v in d.items():
	if v != 0:
		p *= (k**v)
print(p)
print(time.time() - start, "sec")

# Method 2: Exec time: 40 secs XD
'''
import time
start = time.time()

def l(a, b):
	if a > b:
		greater = a
	else:
		greater = b
	while True:
		if greater % a == 0 and greater % b == 0:
			return greater
		else:
			greater += 1

lcm = 1
for i in range(2, 21):
	lcm = l(lcm, i)

print(lcm)
print(time.time() - start, "sec")
'''
