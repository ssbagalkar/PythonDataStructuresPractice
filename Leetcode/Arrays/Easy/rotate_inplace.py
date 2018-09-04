## Rotate 1D array by r elements on right in place
## 

def rotate(nums, k):
	n = len(nums)
	k = k % n
	nums[:] = nums[n-k:] + nums[:n-k]
	return nums

print(rotate([1,2,3,4,5],-2))

	
	