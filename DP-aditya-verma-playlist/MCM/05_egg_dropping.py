"""
# Problem statement:
https://www.includehelp.com/algorithms/egg-dropping-problem-using-dynamic-programming.aspx

Video:
https://www.youtube.com/watch?v=S49zeUjeUL0&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=43&ab_channel=AdityaVermaAdityaVerma


Leetcode:

You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.


Good explanation of solution on leetcode:
https://leetcode.com/problems/super-egg-drop/discuss/792736/CPP-Explained-Recursive-greatermemoization-greateroptimization-greaterDP-oror-Well-Explained-oror-Easy-to-unserstand
Recursion Complexity:
Time Complexity: O(n * (2^min(n,k))
Space Complexity: O(1) , If we ignore space taken by stack frame

Memoized Complexity:
Time Complexity: O((n^2) * k)
Space Complexity: O(k * n)

Optimized Memoized Complexity:
Time Complexity: O((n * k) * logn )
Space Complexity: O(n * k)

Verified in Leetcode/other platform?

Recursive solution exceeds time limit. Though, it does not fail. Passed 31/121 test cases for recursive
"""


def egg_dropping_recursive(e, f):
	# Base condition:
	if e <= 1 or f <= 1:
		return f

	# declare int_max
	min_val = float("inf")

	for k in range(1, f+1):
		temp_val = 1 + max(egg_dropping_recursive(e-1, k-1), egg_dropping_recursive(e, f-k))
		if temp_val < min_val:
			min_val = temp_val
	return min_val


def egg_dropping_memo(e, f, memo):

	if memo[e][f] != -1:
		return memo[e][f]

	# Base condition:
	if e <= 1 or f <= 1:
		return f

	# declare int_max
	min_val = float("inf")

	for k in range(1, f+1):
		temp_val = 1 + max(egg_dropping_memo(e-1, k-1, memo), egg_dropping_memo(e, f-k, memo))
		if temp_val < min_val:
			min_val = temp_val
	memo[e][f] = min_val
	return min_val


def egg_dropping_memo_optimized(e, f, memo):

	if memo[e][f] != -1:
		return memo[e][f]

	# Base condition:
	if e <= 1 or f <= 1:
		return f

	# declare int_max
	min_val = float("inf")

	for k in range(1, f+1):
		if memo[e-1][k-1] != -1:
			lower = memo[e-1][k-1]
		else:
			lower = egg_dropping_memo(e-1, k-1, memo)
		if memo[e][f-k] != -1:
			upper = memo[e][f-k]
		else:
			upper = egg_dropping_memo(e, f - k, memo)
		temp_val = 1 + max(lower, upper)
		if temp_val < min_val:
			min_val = temp_val
	memo[e][f] = min_val
	return min_val

num_eggs = 3
num_floors = 14
print(egg_dropping_recursive(num_eggs, num_floors))

memo = [[-1 for _ in range(num_floors+1)] for _ in range(num_eggs+1)]
print(egg_dropping_memo(num_eggs, num_floors, memo))
print(egg_dropping_memo_optimized(num_eggs, num_floors,memo))
