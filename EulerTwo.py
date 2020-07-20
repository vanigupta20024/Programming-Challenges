# Project Euler: Problem 2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

sum = 0
f = 1
s = 2
x = s
while x < 4000000:
	if x % 2 == 0:
		sum += x
	x = f + s
	f, s = s, x

print(sum)
