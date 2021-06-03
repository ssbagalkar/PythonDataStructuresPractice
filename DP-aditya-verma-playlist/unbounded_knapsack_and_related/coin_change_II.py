"""
Video --> https://www.youtube.com/watch?v=I-l6PBeERuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=16
Problem Statement -> Given an array of coins and an integer, find the minimum number of coins to get the integer

In this problem - Initialization is different, else very similar to subset sum
"""

def coin_change_min_ways_recursive(coin_arr, s, n):
    # Initialization is different
    if s == 0:
        return 0
    if n == 0:
        return float("inf")

    if s >= coin_arr[n-1]:
        return min(1+coin_change_min_ways_recursive(coin_arr, s-coin_arr[n-1], n),
                   coin_change_min_ways_recursive(coin_arr, s, n-1))
    elif s < coin_arr[n-1]:
        return coin_change_min_ways_recursive(coin_arr, s, n-1)


def coin_change_min_ways_tabular(coin_arr, s, n):
    dp = [[0 for _ in range(s+1)] for _ in range(n+1)]

    for jj in range(s+1):
        dp[0][jj] = float("inf")

    for ii in range(1, n+1):
        for jj in range(1, s+1):
            if jj >= coin_arr[ii-1]:
                dp[ii][jj] = min(1+dp[ii][jj-coin_arr[ii-1]], dp[ii-1][jj])
            elif jj < coin_arr[ii-1]:
                dp[ii][jj] = dp[ii-1][jj]
    return dp[n][s]



coin_arr = [1, 2, 3]
s = 5
expected = 2
n = len(coin_arr)
# print(coin_change_min_ways_recursive(coin_arr, s, n))
print(coin_change_min_ways_tabular(coin_arr, s, n))

