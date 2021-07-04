"""
Video -> https://www.youtube.com/watch?v=uUXXEgK2Jh8&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=4&ab_channel=AdityaVermaAdityaVerma
Problem --> https://www.geeksforgeeks.org/first-negative-integer-every-window-size-k/

Complexity:
Method                            Time (worst)     Auxiliary Space(worst)   Passing tests?
first_neg_number_not_optimized        O(n*k)           O(k)                     Yes, with TLE
"""

from collections import deque
def first_negative_number_sliding(arr, k):
    n = len(arr)
    neg_values=[]
    for ii in range(n-k+1):
        jj = ii
        while jj < (ii + k) :
            if arr[jj] >= 0:
                if jj == ii + k - 1:
                    neg_values.append(0)
                jj+=1
            else:
                neg_values.append(arr[jj])
                break

    return neg_values


def first_negative_number_optimized(nums, n, k):
	if len(nums) == 0:
		return None
	if len(nums) == 1:
		if nums[0] < 0:
			return nums[0]
		else:
			return None

	deq = deque()
	for ii in range(k):
		if nums[ii] < 0:
			deq.append(ii)

	for ii in range(k, n):
		if len(deq) > 0:
			print(f"{nums[deq[0]]}", end=" ")
		else:
			print("0", end=" ")

		# delete all indexes in the deque which are less than bounds of the current window
		while deq and deq[0] <= ii - k:
			deq.popleft()

		if nums[ii] < 0:
			deq.append(ii)
	if not deq:
		print(0)
	else:
		print(nums[deq[0]], end=" ")



print(first_neg_number_not_optimized([12, -1, -7, 8, -15, 30, 16, 28], 8, 3))
first_negative_number_optimized([12, -1, -7, 8, -15, 30, 16, 28], 8, 3)