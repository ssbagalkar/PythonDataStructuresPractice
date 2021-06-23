

"""
Not verified yet
"""
def largest_subarray_brute(arr, to_find):
	if sum(arr) < to_find:
		return -1
	if sum(arr) == to_find:
		return arr
	n = len(arr)
	result = []
	for ii in range(n):
		for jj in range(ii, n+1):
			if sum(arr[ii:jj]) > to_find:
				break
			elif sum(arr[ii:jj]) < to_find:
				continue
			else:
				result.append(arr[ii:jj])
	max_result = max([len(ans) for ans in result])
	return max_result


def largest_subarray_optimized(arr, target_sum):
	if sum(arr) < target_sum:
		return -1
	if sum(arr) == target_sum:
		return arr
	n = len(arr)
	result = float("-inf")
	ii = 0
	jj = 1
	while jj < n:
		current_sum = sum(arr[ii:jj])
		if current_sum == target_sum:
			result = max(result, jj - ii)

			jj += 1
		elif current_sum < target_sum:
			jj += 1
		else:
			while current_sum > target_sum:
				current_sum = current_sum - arr[ii]
				ii += 1
	return result


arr = [4, 1, 1, 1, 2, 3, 5]
print(largest_subarray_brute(arr, 5))
print(largest_subarray_optimized([4, 1, 1, 1, 2, 3, 5], 5))