"""
Video -->https://www.youtube.com/watch?v=F7wqWbqYn9g&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=9
"""


def count_of_subset_sum_recursive(arr, n, s):
    # Base Condition
    if n == 0 and s != 0:
        return 0
    if s == 0:
        return 1

    if s >= arr[n-1]:
        return count_of_subset_sum_recursive(arr, n-1, s-arr[n-1]) + (count_of_subset_sum_recursive(arr, n-1, s))
    elif s < arr[n-1]:
        return count_of_subset_sum_recursive(arr, n-1, s)


def count_of_subset_memoized(arr, n, s):
    memo = [[0 for _ in range(s+1)] for _ in range(n+1)]
    return count_of_subset_memoized_util(arr, n, s, memo)


def count_of_subset_memoized_util(arr, n, s, memo):

    if memo[n][s] != 0:
        return memo[n][s]

    if n == 0 and s != 0:
        return 0

    if s == 0:
        return 1

    if s >= arr[n - 1]:
        memo[n][s] = count_of_subset_memoized_util(arr, n - 1, s - arr[n - 1], memo) + \
                     count_of_subset_memoized_util(arr, n - 1, s, memo)

    elif s < arr[n - 1]:
        memo[n][s] = count_of_subset_memoized_util(arr, n - 1, s, memo)

    return memo[n][s]


def count_of_subset_tabular(arr, n, s):
    dp = [[0 for _ in range(s + 1)] for _ in range(n + 1)]

    for ii in range(n+1):
        dp[ii][0] = 1

    for ii in range(1, n+1):
        for jj in range(1, s+1):
            if jj >= arr[ii-1]:
                dp[ii][jj] = dp[ii-1][jj-arr[ii-1]] + dp[ii-1][jj]
            elif jj < arr[ii-1]:
                dp[ii][jj] = dp[ii-1][jj]
    return dp[n][s]


arr = [2, 3, 5, 6, 8, 10]
n = len(arr)
s = 18
expected = 4
assert count_of_subset_sum_recursive(arr, n, s) == expected
assert count_of_subset_memoized(arr, n, s) == expected
assert count_of_subset_memoized(arr, n, s) == count_of_subset_sum_recursive(arr, n, s)
assert count_of_subset_tabular(arr, n, s) == expected
assert count_of_subset_tabular(arr, n, s) == count_of_subset_sum_recursive(arr, n, s)
print("All test passed")
