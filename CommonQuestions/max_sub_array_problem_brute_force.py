## this is naive brute-force method. Not effective
import math

def max_subarray_problem(arr1):
	n = len(arr1)
	max_sum_array = [-math.inf]
	current_array=[]
	for ii in range(n):
	current_array=[]
		current_array.append[ii]
		if sum(current_array) > max_sum_array:
			max_sum_array = current_array
		for jj in range(ii+1,n):
			current_array.append[jj]
			if sum(current_array) > sum(max_sum_array):
				max_sum_array = current_array
				
	return max_sum_array
	
	
arr = [1, -3, 2, 1, -1]
print(max_subarray_problem(arr))