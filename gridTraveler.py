def grid_traveler(m, n, memo = {}):
	key = str(m) + "," + str(n)
	if key in memo.keys():
		return memo[key]
	if key[::-1] in memo.keys():
		return memo[key[::-1]]
	if m == 0 or n == 0:
		return 0
	if m == 1 and n == 1:
		return 1

	memo[key] = grid_traveler(m, n - 1, memo) + grid_traveler(m - 1, n, memo)

	return memo[key]

print(grid_traveler(2, 3))
print(grid_traveler(1, 3))
print(grid_traveler(7, 8))
print(grid_traveler(10, 10))
print(grid_traveler(13, 19))
