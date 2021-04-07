def how_sum(target_sum, numbers, memo={}):
	if target_sum in memo.keys():
		return memo[target_sum]
	if target_sum == 0: return []
	if target_sum < 0: return None

	for num in numbers:
		remainder = target_sum - num
		rem_result = how_sum(remainder, numbers, memo)
		if rem_result is not None:
			memo[target_sum] = rem_result + [num]
			return memo[target_sum]
	memo[target_sum] = None
	return None

print(how_sum(300, [2,3]))
