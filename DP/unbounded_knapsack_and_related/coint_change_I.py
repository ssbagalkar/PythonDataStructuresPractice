"""
Video Link --> https://www.youtube.com/watch?v=I4UR2T6Ro3w&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=15

VERY SIMILAR TO SUBSET SUM PROBLEM! JUST CHANGE n-1 to n and use a +
"""


def coin_change_max_ways_recursion(coin_arr, s, n):

    if n == 0 and s != 0:
        return 0
    if s == 0:
        return 1

    if coin_arr[n-1] <= s:
        return coin_change_max_ways_recursion(coin_arr, s-coin_arr[n-1], n)+ coin_change_max_ways_recursion(coin_arr, s, n-1)

    elif coin_arr[n-1] > s:
        return coin_change_max_ways_recursion(coin_arr, s, n-1)

"""
Let's memoize the above solution
"""


def coin_change_max_ways_memoization(arr, s, n, memo):

    if memo[n][s] != 0:
        return memo[n][s]

    if n == 0 and s != 0:
        return False
    if s == 0:
        return True

    if arr[n-1] <= s:
        memo[n][s] = coin_change_max_ways_memoization(arr, s-arr[n-1], n, memo) + coin_change_max_ways_memoization(arr, s, n-1, memo)

    elif arr[n-1] > s:
        memo[n][s] = coin_change_max_ways_memoization(arr, s, n-1, memo)

    return memo[n][s]

"Let's make this DP table"
def coin_change_max_ways_tabular(arr, s, n):
    dp = [[False for _ in range(s + 1)] for _ in range(n + 1)]

    # If sum is 0, then answer is true
    for ii in range(n + 1):
        dp[ii][0] = True

    for ii in range(1, n+1):
        for jj in range(1, s+1):
            if arr[ii-1] <= jj:
                dp[ii][jj] = dp[ii][jj-arr[ii-1]] + dp[ii-1][jj]
            elif arr[ii-1] > jj:
                dp[ii][jj] = dp[ii-1][jj]
    return dp[n][s]


coin_arr = [1, 2, 3]
s = 5
expected = 5
memo = [[0 for _ in range(s+1)] for _ in range(len(coin_arr)+1)]
print(f"Answer using Recursion --> {coin_change_max_ways_recursion(coin_arr, s, len(coin_arr))}")
print(f"Answer using Memoization --> {coin_change_max_ways_memoization(coin_arr, s, len(coin_arr), memo)}")
print(f"Answer using DP --> {coin_change_max_ways_tabular(coin_arr, s, len(coin_arr))}")
assert coin_change_max_ways_recursion(coin_arr, s, len(coin_arr)) == \
       coin_change_max_ways_memoization(coin_arr, s, len(coin_arr), memo)
assert coin_change_max_ways_recursion(coin_arr, s, len(coin_arr)) == \
       coin_change_max_ways_tabular(coin_arr, s, len(coin_arr))
print("all tests passed")
