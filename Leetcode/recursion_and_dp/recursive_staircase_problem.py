#https://www.youtube.com/watch?v=5o-kdjv7FD0&t=1s

#Brute force recursion
# time --> O(2^n)
# space --> O(1)


def num_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)

# memoization
# Time --> O(n)
# Space --> O(n)


memo = {}


def num_ways_memoized(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    memo[n] = num_ways_memoized(n-1) + num_ways_memoized(n-2)
    return memo[n]

# DP approach
def num_ways_bottom_up (n):
    if n == 0 or n == 1:
        return 1
    nums = [-1 for _ in range(n+1)]
    nums[0] = 1
    nums[1] = 1
    for ii in range(2, n+1):
        nums[ii] = nums[ii-1] + nums[ii-2]
    return nums[n]

# brute force approach generalized for n
def num_ways_generalized(n,X):
    if n == 0:
        return 1
    total = 0
    for ii in X:
        if n - ii >= 0:
            total+=num_ways_generalized(n-ii, X)
    return total

def num_ways_generalized_bottom_up(n,X):
    if n == 0:
        return 1
    dp = [-1 for _ in range(n+1)]
    dp[0] = 1
    for ii in range(1, n+1):
        total = 0
        for jj in (X):
            if ii - jj >= 0:
                total+=dp[ii-jj]
            dp[ii] = total
    return dp[n]

n = 4
X = [1, 3, 5]
assert num_ways(4) == num_ways_bottom_up(4) == num_ways_memoized(n)
print(num_ways_memoized(n))
assert num_ways_generalized(n, X) == num_ways_generalized_bottom_up(n, X)
print(num_ways_generalized_bottom_up(n, X))