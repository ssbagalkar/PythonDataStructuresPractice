# """
# Problem Statement
# =================
#
# 0/1 Knapsack Problem - Given items of certain weights/values and maximum allowed weight how to pick items to pick items
# from this set to maximize sum of value of items such that sum of weights is less than or equal to maximum allowed
# weight.
#
# Runtime Analysis
# ----------------
# Time complexity - O(n*s)
#
# Video
#
# Refer this series for DP --> https://www.youtube.com/watch?v=kvyShbFVaY8&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=3

# References
# ----------
# * http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/
# * https://en.wikipedia.org/wiki/Knapsack_problem
# """


def knapsack_0_1_recursive(weights, values, n, total_weight):
    # Base condition
    if n == 0 or total_weight == 0:
        return 0
    if weights[n-1] <= total_weight:
        return max(values[n-1] + knapsack_0_1_recursive(weights, values, n-1, total_weight-weights[n-1]),
                   knapsack_0_1_recursive(weights, values, n-1, total_weight))
    elif weights[n-1] > total_weight:
        return knapsack_0_1_recursive(weights, values, n-1, total_weight)


def knapsack_0_1_memoization(weights, values, n, total_weight):
    memo = [[0 for _ in range(total_weight+1)] for _ in range(n+1)]
    return knapsack_0_1_memoization_util(weights, values, n, total_weight, memo)


def knapsack_0_1_memoization_util(weights, values, n, total_weight, memo):
    # Check if value already exists
    if memo[n][total_weight] != 0:
        return memo[n][total_weight]

    # Base condition
    if n == 0 or total_weight == 0:
        return 0

    if weights[n-1] <= total_weight:
        memo[n][total_weight] = max(values[n-1] +
                                    knapsack_0_1_memoization_util(weights, values, n-1, total_weight-weights[n-1], memo),
                                    knapsack_0_1_memoization_util(weights, values, n-1, total_weight, memo))

    elif weights[n-1] > total_weight:
        memo[n][total_weight] = knapsack_0_1_memoization_util(weights, values, n-1, total_weight, memo)

    return memo[n][total_weight]


def knapsack_0_1_dp(weights, values, total_weight):
    n = len(weights)
    dp = [[0 for _ in range(total_weight+1)] for _ in range(n+1)]

    for ii in range(1, n+1):
        for jj in range(1, total_weight+1):
            if weights[ii-1] <= jj:
                dp[ii][jj] = max(values[ii-1] + dp[ii-1][jj-weights[ii-1]], dp[ii-1][jj])
            elif weights[ii-1] > jj:
                dp[ii][jj] = dp[ii-1][jj]
    return dp[n][total_weight]


if __name__ == '__main__':
    total_weight = 8
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    expected = 11
    assert expected == knapsack_0_1_recursive(weights, values, len(weights), total_weight)
    assert expected == knapsack_0_1_memoization(weights, values, len(weights), total_weight)
    assert knapsack_0_1_memoization(weights, values, len(weights), total_weight) == \
           knapsack_0_1_recursive(weights, values, len(weights), total_weight)
    assert expected == knapsack_0_1_dp(weights, values, total_weight)
    assert knapsack_0_1_dp(weights, values, total_weight) == knapsack_0_1_memoization(weights, values, len(weights), total_weight)

