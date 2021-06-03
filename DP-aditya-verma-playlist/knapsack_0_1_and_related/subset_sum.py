"""
Problem - https://www.youtube.com/watch?v=kvyShbFVaY8&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=3

# Let's do it 3 ways -
1. recursion
2. memoization
3. tabular
"""
import math
# recursive solution - time complexity --> O(2^n) and space is ??


def subset_sum_recursion(arr, s, n):

    if n == 0 and s != 0:
        return False
    if s == 0:
        return True

    if arr[n-1] <= s:
        return subset_sum_recursion(arr, s-arr[n-1], n-1) or subset_sum_recursion(arr, s, n-1)

    elif arr[n-1] > s:
        return subset_sum_recursion(arr, s, n-1)

"""
Let's memoize the above solution
"""


def subset_sum_memoization(arr, s, n, memo):

    if memo[n][s] != 0:
        return memo[n][s]

    if n == 0 and s != 0:
        return False
    if s == 0:
        return True

    if arr[n-1] <= s:
        memo[n][s] = subset_sum_memoization(arr, s-arr[n-1], n-1, memo) or subset_sum_memoization(arr, s, n-1, memo)

    elif arr[n-1] > s:
        memo[n][s] = subset_sum_memoization(arr, s, n-1, memo)

    return memo[n][s]

"Let's make DP table"
def subset_sum_tabular(arr, s, n):
    dp = [[False for _ in range(s + 1)] for _ in range(n + 1)]

    # If sum is 0, then answer is true
    for ii in range(n + 1):
        dp[ii][0] = True

    for ii in range(1, n+1):
        for jj in range(1, s+1):
            if arr[ii-1] <= jj:
                dp[ii][jj] = dp[ii-1][jj-arr[ii-1]] or dp[ii-1][jj]
            elif arr[ii-1] > jj:
                dp[ii][jj] = dp[ii-1][jj]
    return dp[n][s]



arr = [2, 3, 7, 8, 10]
s = 10
n = len(arr)
memo = [[0 for _ in range(s+1)] for _ in range(n+1)]
expected = True
assert subset_sum_recursion(arr, s, n) == expected
assert subset_sum_memoization(arr, s, n, memo) == expected
assert subset_sum_tabular(arr, s, n)
assert subset_sum_recursion(arr, s, n) == subset_sum_memoization(arr, s, n, memo)

