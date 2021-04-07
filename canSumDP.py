def canSum(target_sum, numbers, memo = {}):
	if target_sum in memo.keys():
		return memo[target_sum]
	if target_sum == 0: return True
	if target_sum < 0: return False

	for num in numbers:
		remainder = target_sum - num
		if canSum(remainder, numbers, memo) == True:
			memo[target_sum] = True
			return True
	memo[target_sum] = False
	return False


print(canSum(7, [2,3]))
print(canSum(13, [3,4,5,81]))
print(canSum(30, [11, 13]))
