"""
Video--> https://www.youtube.com/watch?v=KtpqeN0Goro&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=3&ab_channel=AdityaVermaAdityaVerma
Link --> https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
Optimized solution from Leetcode --> https://leetcode.com/problems/sliding-window-maximum/solution/
Method                     Time          Space
find_sliding_max_naive     O(n*k)          O(1)-> if just printing or O(N-k+1) -> if returning
find_sliding_max_optimized O(n)            O(n)
"""
from collections import deque


def find_sliding_max_naive(arr, n, k):
	"""
	Just take 2 loops and find all sums and take max
	"""
	for ii in range(n - k + 1):
		jj = ii
		current_sum = float("-inf")
		while jj < ii + k:
			if arr[jj] > current_sum:
				current_sum = arr[jj]
			jj += 1
		print(current_sum, end = " ")
	print("")


# Having spent hours to properly understand, I do not grasp this. Look at the alternative geeks implementation
def find_sliding_max_optimized(nums, k):
	"""
	The algorithm is quite straightforward :

		1. Process the first k elements separately to initiate the deque.

		2. Iterate over the array. At each step :

			2a. Clean the deque :

				a. Keep only the indexes of elements from the current sliding window.

				b. Remove indexes of all elements smaller than the current one, since they will not be the maximum ones.

			2b. Append the current element to the deque.

			2c. Append deque[0] to the output.

		3. Return the output array.

	Note : You want to ensure the deque window only has decreasing elements. That way, the leftmost element is always the largest.
	"""
	# base cases
	n = len(nums)
	if n * k == 0:
		return []
	if k == 1:
		return nums

	def clean_deque(i):
		# remove indexes of elements not from sliding window
		if deq and deq[0] == i - k:
			deq.popleft()

		# remove from deq indexes of all elements
		# which are smaller than current element nums[i]
		while deq and nums[i] > nums[deq[-1]]:
			deq.pop()

	# init deque and output
	deq = deque()
	max_idx = 0
	for i in range(k):
		clean_deque(i)
		deq.append(i)
		# compute max in nums[:k]
		if nums[i] > nums[max_idx]:
			max_idx = i
	# output = [nums[max_idx]]
	print(f"{nums[deq[0]]}", end=" ")

	# build output
	for i in range(k, n):
		clean_deque(i)
		deq.append(i)
		# output.append(nums[deq[0]])
		print(f"{nums[deq[0]]}", end=" ")
	print("")
	# return output


def find_sliding_max_optimized_geeks_version(nums, k):
	if len(nums) == 0:
		print("Empty array")
	if len(nums) == 1:
		print(f"{nums[0]}")

	deq = deque()

	# Process first k (or first window)
	# elements of array
	for ii in range(k):

		# For every element, the previous
		# smaller elements are useless
		# so remove them from deque
		while deq and nums[ii] >= nums[deq[-1]]:
			deq.pop()

		# Add new element at rear of queue
		deq.append(ii)

	# Process rest of the elements, i.e.
	# from arr[k] to arr[n-1]
	for ii in range(k, n):

		# The element at the front of the
		# queue is the largest element of
		# previous window, so print it
		print(f"{nums[deq[0]]}", end=" ")

		# Remove the elements which are
		# out of this window
		while deq and deq[0] <= ii - k:
			deq.popleft()

		# Remove all elements smaller than
		# the currently being added element
		# (Remove useless elements)
		while deq and nums[ii] >= nums[deq[-1]]:
			deq.pop()

		# Add current element at the rear of Qi
		deq.append(ii)
	print(f"{nums[deq[0]]}", end="")


arr = [1, 3, -1, -3, 5, 3, 6, 7]
n = len(arr)
k = 3
find_sliding_max_naive(arr, n, k)
find_sliding_max_optimized(arr, k)
find_sliding_max_optimized_geeks_version(arr, k)