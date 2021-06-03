"""
Problem: Given a sequence, find the length of the longest palindromic subsequence in it.
Example :
Input:"bbbab"
Output:4
Input:"agbcba"
output:5 ( abcba)

Note: EXACTLY SIMILAR TO LCS, JUST PASS ONE MORE STRING WHICH IS PALINDROME OF THE FIRST
Complexity Analysis:
n is length of longest string
                Time                Space
Recursion       O(2^n)              O(1)

Memoization     O(m*n)              O(n * m)

Tabular         O(m*n)              O(n * m ) ?

Answers verified in Leetcode/HackerRank? : ?
"""

def lps_recursion(s1, s2, n, m):
    # Base condition
    if n == 0 or m == 0:
        return 0

    if s1[n-1] == s2[m-1]:
        return 1 + lps_recursion(s1, s2, n-1, m-1)
    else:
        return max(lps_recursion(s1, s2, n, m-1), lps_recursion(s1, s2, n-1, m))

def lps_memoization(s1, s2, n, m, memo):

    # check memo table
    if memo[n][m] != 0:
        return memo[n][m]

    # Base condition
    if n == 0 or m == 0:
        return 0

    if s1[n-1] == s2[m-1]:
        memo[n][m] =1 + lps_recursion(s1, s2, n-1, m-1)
    else:
        memo[n][m] = max(lps_recursion(s1, s2, n, m-1), lps_recursion(s1, s2, n-1, m))
    return memo[n][m]


def lps_tabular(s1, s2, n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for ii in range(1, n+1):
        for jj in range(1, m+1):
            if s1[ii-1] == s2[jj-1]:
                dp[ii][jj] = 1 + dp[ii-1][jj-1]
            else:
                dp[ii][jj] = max(dp[ii][jj-1], dp[ii-1][jj])
    return dp[n][m]

s1 = "agbcba"
s2 = s1[::-1]
n = len(s1)
m = len(s2)
print(lps_recursion(s1, s2, n, m))
memo = [[0 for _ in range(m+1)] for _ in range(n+1)]
print(lps_memoization(s1, s2, n, m, memo))
assert lps_recursion(s1, s2, n, m) == lps_memoization(s1, s2, n, m, memo)
print("LCS recursion and LCS memoization matches")
print(lps_tabular(s1, s2, n, m))
assert lps_memoization(s1, s2, n, m, memo) == lps_recursion(s1, s2, n, m)
print("LCS memoization and LCS tabular  matches")



