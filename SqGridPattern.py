# GHC Codepath SE101 
# level basic to intermediate

# Grid of numbers in a pattern as follows:
# input: 4
# output:
# [0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 0]
# [0, 1, 2, 2, 2, 2, 2, 1, 0]
# [0, 1, 2, 3, 3, 3, 2, 1, 0]
# [0, 1, 2, 3, 4, 3, 2, 1, 0]
# [0, 1, 2, 3, 3, 3, 2, 1, 0]
# [0, 1, 2, 2, 2, 2, 2, 1, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0]

n = int(input())
if n < 1:
	print("Enter a larger number!")
	exit()

current = 0
low = 0
high = 2 * n + 1
a = [[0 for i in range(high)] for j in range(high)]

while low < high:
	for i in range(low, high):
		for j in range(low, high):
			a[i][j] = current

	current += 1
	low += 1
	high -= 1

for i in a:
	print(i)
