# Following is brute force 0(n^3) complexity
def find132pattern(nums):
	if sorted(nums) == nums:
		return False
	
	for ii in range(len(nums) - 2):
		for jj in range(ii+1, len(nums) - 1):
			for kk in range(jj+1, len(nums)):
				if nums[ii] < nums[kk] < nums[jj]:
					return True
	return False
				
print(find132pattern([5, 4, 3, 2]))

#https://leetcode.com/articles/132-pattern/