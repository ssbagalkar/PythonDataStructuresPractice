#https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
# We will first sort the fix the first element and find the other two
# Complexity is O(n^2)
def find_triplet(num_list, sum_to_find):
	num_list = sorted(num_list)
	
	for ii in range(len(num_list)-2):
		
		left_idx = ii+1
		right_idx = len(num_list)-1
		
		while(left_idx<right_idx):
			current_sum = num_list[left_idx] + num_list[right_idx] + num_list[ii]
			if sum_to_find > current_sum:
				left_idx+=1
			elif sum_to_find < current_sum:
				right_idx-=1
			else:
				return ([num_list[ii], num_list[left_idx], num_list[right_idx]])
	return -1

num_list = [1, 4, 45, 6, 10, 8]	
sum_to_find = 56

print(find_triplet(num_list, sum_to_find))