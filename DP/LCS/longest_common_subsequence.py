"""
Problem statement:Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

For example, “abc”,  “abg”, “bdf”, “aeg”,  ‘”acefg”, .. etc are subsequences of “abcdefg”.
PROBLEM STATEMENT LINK:https://www.geeksforgeeks.org/longest...
Youtube Video (Aditya Verma)-->https://www.youtube.com/watch?v=4Urd0a0BNng&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=19

Complexity Analysis:
                Time    Space
Recursion

Memoization

Tabular
"""

def lcs_recursion(str_one, str_two, n, m):

    # Base condition
    if n == 0 or m == 0:
        return 0

    # From choice diagram
    if str_one[n-1] == str_two[m-1]:
        return 1 + lcs_recursion(str_one, str_two, n-1, m-1)
    else:
        return max(lcs_recursion(str_one, str_two, n-1, m), lcs_recursion(str_one, str_two, n, m-1))


def lcs_memoization(str_one, str_two, n, m, memo):
    # Base Condition and checking
    if memo[n][m] != 0:
        return memo[n][m]
    if n == 0 or m == 0:
        return 0

    # From choice diagram
    if str_one[n - 1] == str_two[m - 1]:
        memo[n][m] = 1 + lcs_memoization(str_one, str_two, n - 1, m - 1, memo)
    else:
        memo[n][m] = max(lcs_memoization(str_one, str_two, n - 1, m, memo),
                         lcs_memoization(str_one, str_two, n, m - 1, memo))
    return memo[n][m]



str_one = "AGGTAB"
str_two = "GXTXAYB"
n = len(str_one)
m = len(str_two)
print(lcs_recursion(str_one, str_two, n, m))
memo = [[0 for _ in range(m+1)] for _ in range(n+1)]
print(lcs_memoization(str_one, str_two, n, m, memo))
assert lcs_recursion(str_one, str_two, n, m) == lcs_memoization(str_one, str_two, n, m, memo)
print("LCS recursion and LCS memoization matches")
