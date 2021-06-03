"""
EXACTLY similar to LCS--> just add lengths of both strings and then subtract LCS
Problem statement:Given two strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences.

Input:   str1 = "geek",  str2 = "eke"
Output: 4 --> "geeke"
PROBLEM STATEMENT LINK:https://www.geeksforgeeks.org/shortest-common-supersequence/
Youtube Video for LCS (Aditya Verma)-->https://www.youtube.com/watch?v=823Grn4_dCQ&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=24

Complexity Analysis:
n is length of longest string (Verify)
                Time                Space
Recursion       O(2^n)              O(1)

Memoization     O(m*n)              O(n * m)

Tabular         O(m*n)              O(n * m ) ?

Answers verified in Leetcode/HackerRank? : No
"""


def scs_recursion(str_one, str_two, n, m):
    # Base condition
    if n == 0 or m == 0:
        return 0

    # From choice diagram
    if str_one[n-1] == str_two[m-1]:
        return 1 + scs_recursion(str_one, str_two, n-1, m-1)
    else:
        return max(scs_recursion(str_one, str_two, n-1, m), scs_recursion(str_one, str_two, n, m-1))


def scs_memoization(str_one, str_two, n, m, memo):
    # Base Condition and checking
    if memo[n][m] != 0:
        return memo[n][m]
    if n == 0 or m == 0:
        return 0

    # From choice diagram
    if str_one[n - 1] == str_two[m - 1]:
        memo[n][m] = 1 + scs_memoization(str_one, str_two, n - 1, m - 1, memo)
    else:
        memo[n][m] = max(scs_memoization(str_one, str_two, n - 1, m, memo),
                         scs_memoization(str_one, str_two, n, m - 1, memo))
    return memo[n][m]


def print_lcs_tabular(str_one, str_two, n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for ii in range(1, n+1):
        for jj in range(1, m+1):
            if str_one[ii-1] == str_two[jj-1]:
                dp[ii][jj] = 1 + dp[ii-1][jj-1]
            else:
                dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1])
    return dp[n][m]


str_one = "AGGTAB"
str_two = "GXTXAYB"
n = len(str_one)
m = len(str_two)
print(f"Recursion Result --> {len(str_one) + len(str_two) - scs_recursion(str_one, str_two, n, m)}")
memo = [[0 for _ in range(m+1)] for _ in range(n+1)]
print(f"Memoization Result --> {len(str_one) + len(str_two) - scs_memoization(str_one, str_two, n, m, memo)}")
assert len(str_one) + len(str_two) - scs_recursion(str_one, str_two, n, m) == len(str_one) + len(str_two) -scs_memoization(str_one, str_two, n, m, memo)
print("SCS recursion and SCS memoization matches")
print(f"Tabular Result --> {len(str_one) + len(str_two) - print_lcs_tabular(str_one, str_two, n, m)}")
assert len(str_one) + len(str_two) - scs_memoization(str_one, str_two, n, m, memo) == len(str_one) + len(str_two) -scs_recursion(str_one, str_two, n, m)
print("SCS memoization and SCS tabular  matches")
