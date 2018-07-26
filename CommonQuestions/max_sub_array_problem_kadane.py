## better solution using kadane algorithm
from copy import deepcopy
def max_subarray_kadane(arr):
	max_current = [arr[0]]
	max_global = [arr[0]]
	n = len(arr)
	
	for ii in range(1, n):
		max_sum = max(arr[ii], sum(max_current) + arr[ii])
		if max_sum != arr[ii]:
			max_current.append(arr[ii])
		else:
			max_current=[arr[ii]]
		if sum(max_current) > sum(max_global):
			max_global = deepcopy(max_current)
	
	return max_global


arr = [-2, 1, 2, -1]
print(max_subarray_kadane(arr))