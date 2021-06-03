"""

NOTE: VERY SIMILAR TO PREVIOUS PROBLEM. NOW, INSTEAD OF FINDING THE LENGTH OF LONGEST SEQUENCE, YOU EVEN HAVE TO PRINT THE SEQUENCE
Problem statement:Given two sequences, find and PRINT the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

For example, “abc”,  “abg”, “bdf”, “aeg”,  ‘”acefg”, .. etc are subsequences of “abcdefg”.
PROBLEM STATEMENT LINK:https://www.geeksforgeeks.org/printing-longest-common-subsequence/.
Youtube Video for LCS (Aditya Verma)-->https://www.youtube.com/watch?v=4Urd0a0BNng&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=19

Complexity Analysis:
n is length of longest string
                Time                Space
Recursion       O(2^n)              O(1)

Memoization     O(m*n)              O(n * m)

Tabular         O(m*n)              O(n * m ) ?

Answers verified in Leetcode/HackerRank? : Yes
"""


def print_lcs_recursion(str_one, str_two, n, m):
    # Base condition
    if n == 0 or m == 0:
        return ""

    # From choice diagram
    if str_one[n-1] == str_two[m-1]:
        return str_one[n-1] + print_lcs_recursion(str_one, str_two, n-1, m-1)
    else:
        return max(print_lcs_recursion(str_one, str_two, n-1, m), print_lcs_recursion(str_one, str_two, n, m-1))


def print_lcs_memoization(str_one, str_two, n, m, memo):
    # Base Condition and checking
    if memo[n][m] != "":
        return memo[n][m]
    if n == 0 or m == 0:
        return ""

    # From choice diagram
    if str_one[n - 1] == str_two[m - 1]:
        memo[n][m] = str_one[n-1] + print_lcs_memoization(str_one, str_two, n - 1, m - 1, memo)
    else:
        memo[n][m] = max(print_lcs_memoization(str_one, str_two, n - 1, m, memo),
                         print_lcs_memoization(str_one, str_two, n, m - 1, memo))
    return memo[n][m]


def print_lcs_tabular(str_one, str_two, n, m):
    dp = [["" for _ in range(m+1)] for _ in range(n+1)]
    for ii in range(1, n+1):
        for jj in range(1, m+1):
            if str_one[ii-1] == str_two[jj-1]:
                dp[ii][jj] = str_one[ii-1] + dp[ii-1][jj-1]
            else:
                dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1])
    return dp[n][m]


str_one = "abcde"
str_two = "ace"
n = len(str_one)
m = len(str_two)
print(f"Recursion Result --> {print_lcs_recursion(str_one, str_two, n, m)[::-1]}")
memo = [["" for _ in range(m+1)] for _ in range(n+1)]
print(f"Memoization Result --> {print_lcs_memoization(str_one, str_two, n, m, memo)[::-1]}")
assert print_lcs_recursion(str_one, str_two, n, m) == print_lcs_memoization(str_one, str_two, n, m, memo)
print("LCS recursion and LCS memoization matches")
print(f"Tabular Result --> {print_lcs_tabular(str_one, str_two, n, m)[::-1]}")
assert print_lcs_memoization(str_one, str_two, n, m, memo)[::-1] == print_lcs_recursion(str_one, str_two, n, m)[::-1]
print("LCS memoization and LCS tabular  matches")
