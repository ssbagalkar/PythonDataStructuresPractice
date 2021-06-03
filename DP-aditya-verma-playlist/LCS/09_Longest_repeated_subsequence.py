"""
Problem Statement:

Longest Repeating Subsequence
Given a string, print the longest repeating subsequence such that the two subsequence don’t have same string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.
Example:
Input: str = "aab"
Output: "a"
The two subsequence are 'a'(first) and 'a'
(second). Note that 'b' cannot be considered
as part of subsequence as it would be at same
index in both.



Exactly similar to LCS with just one minor change. Make sure that the index ii and index jj
are not the same.

Video Link:https://www.youtube.com/watch?v=hbTaCmQGqLg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=30
Geeks link : https://www.geeksforgeeks.org/longest-repeated-subsequence/

Verified on Leetcode: Could not find problem
"""

def lrs_recursion(str_one, str_two, n, m):

    # Base condition
    if n == 0 or m == 0:
        return ""

    # From choice diagram
    if str_one[n-1] == str_two[m-1] and n != m:
        return str_one[n-1] + lrs_recursion(str_one, str_two, n-1, m-1)
    else:
        return max(lrs_recursion(str_one, str_two, n-1, m), lrs_recursion(str_one, str_two, n, m-1))


def lrs_memoization(str_one, str_two, n, m, memo):
    # Base Condition and checking
    if memo[n][m] != 0:
        return memo[n][m]
    if n == 0 or m == 0:
        return ""

    # From choice diagram
    if str_one[n - 1] == str_two[m - 1] and n != m:
        memo[n][m] = str_one[n-1] + lrs_memoization(str_one, str_two, n - 1, m - 1, memo)
    else:
        memo[n][m] = max(lrs_memoization(str_one, str_two, n - 1, m, memo),
                         lrs_memoization(str_one, str_two, n, m - 1, memo))
    return memo[n][m]


def lrs_tabular(str_one, str_two, n, m):
    dp = [["" for _ in range(m+1)] for _ in range(n+1)]
    for ii in range(1, n+1):
        for jj in range(1, m+1):
            if str_one[ii-1] == str_two[jj-1] and ii != jj:
                dp[ii][jj] = str_one[ii-1] + dp[ii-1][jj-1]
            else:
                dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1])
    return dp[n][m]


str_one = "aabebcdd"
str_two = "aabebcdd"
n = len(str_one)
m = len(str_two)
print(lrs_recursion(str_one, str_two, n, m)[::-1])
memo = [[0 for _ in range(m+1)] for _ in range(n+1)]
print(lrs_memoization(str_one, str_two, n, m, memo)[::-1])
print(lrs_tabular(str_one, str_two, n, m)[::-1])
assert lrs_tabular(str_one, str_two, n, m) == lrs_memoization(str_one, str_two, n, m, memo)
assert lrs_tabular(str_one, str_two, n, m) == lrs_recursion(str_one, str_two, n, m)