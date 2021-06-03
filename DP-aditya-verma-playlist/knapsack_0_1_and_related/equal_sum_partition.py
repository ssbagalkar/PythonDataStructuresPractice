"""
Problem link --> https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

Video --> https://www.youtube.com/watch?v=UmMh7xp07kY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=8

"""


def is_equal_recursive_sub(arr, n, s):
    if n == 0 and s != 0:
        return False
    elif s == 0:
        return True
    if arr[n - 1] <= s:
        return is_equal_recursive_sub(arr, n - 1, s - arr[n - 1]) or \
               is_equal_recursive_sub(arr, n - 1, s)
    elif arr[n - 1] > s:
        return is_equal_recursive_sub(arr, n - 1, s)


def is_equal_memoized_sub(arr, n, s, memo):

    if memo[n][s] != 0:
        return memo[n][s]

    if n == 0 and s != 0:
        return False
    elif s == 0:
        return True

    if arr[n - 1] <= s:
        memo[n][s] = is_equal_recursive_sub(arr, n - 1, s - arr[n - 1]) or \
               is_equal_recursive_sub(arr, n - 1, s)
        return memo[n][s]

    elif arr[n - 1] > s:
        memo[n][s] = is_equal_recursive_sub(arr, n - 1, s)
        return memo[n][s]


def is_equal_tabular(arr, n, s, dp):
    for ii in range(1, n+1):
        for jj in range(1, s+1):
            if arr[ii-1] <= jj:
                dp[ii][jj] = dp[ii-1][jj-arr[ii-1]] or dp[ii-1][jj]
            elif arr[ii-1] > jj:
                dp[ii][jj] = dp[ii-1][jj]
    return dp[n][s]


def is_equal(arr, n, mode='recursive'):
    s = sum(arr)
    if s % 2 != 0:
        return False
    if mode == 'recursive':
        return is_equal_recursive_sub(arr, n, s//2)
    if mode == 'memoized':
        memo = [[0 for _ in range(s//2 + 1)] for _ in range(n + 1)]
        return is_equal_memoized_sub(arr, n, s//2, memo)
    else:
        dp = [[False for _ in range(s//2 + 1)] for _ in range(n + 1)]

        # If sum is 0, then answer is true
        for ii in range(n + 1):
            dp[ii][0] = True
        return is_equal_tabular(arr, n, s//2, dp)


arr = [1, 5, 11, 5]
n = len(arr)
expected = True
assert is_equal(arr, n) == True
assert is_equal(arr, n, 'memoized') == True
assert is_equal(arr, n, 'tabular') == True
