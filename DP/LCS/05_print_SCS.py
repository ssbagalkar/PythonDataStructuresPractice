"""
Shortest Common Supersequence
Given two strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences.
Examples:

Input:   str1 = "geek",  str2 = "eke"
Output: "geeke"

Note: I could not find a recursive solution. See the video
https://www.youtube.com/watch?v=VDhRg-ZJTuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=29

Not sure about this! do again
"""


def print_scs_dp(str_one, str_two):
    n = len(str_one)
    m = len(str_two)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    # Build the usual LCS table
    for ii in range(n+1):
        for jj in range(m+1):
            if ii == 0:
                dp[ii][jj] = jj
            elif jj == 0:
                dp[ii][jj] = ii
            elif str_one[ii-1] == str_two[jj-1]:
                dp[ii][jj] = 1 + dp[ii-1][jj-1]
            else:
                dp[ii][jj] = 1 + min(dp[ii-1][jj], dp[ii][jj-1])

    # Now we start printing the SCS
    #dp[n][m] is the cell which holds the SCS string
    output_string = ""
    ii = n
    jj = m
    while ii > 0 and jj > 0:
        if str_one[ii-1] == str_two[jj-1]:
            output_string += str_one[ii-1]
            ii -= 1
            jj -= 1
        else:
            if dp[ii-1][jj] > dp[ii][jj-1]:
                output_string += str_one[ii-1]
                ii -= 1
            elif dp[ii][jj-1] > dp[ii-1][jj]:
                output_string += str_two[jj-1]
                jj -= 1


    while ii > 0:
        output_string += str_one[ii-1]
        ii -= 1
    while jj > 0:
        output_string += str_two[jj-1]
        jj -= 1

    return output_string[::-1]



s1 = "AGGTAB"
s2 = "GXTXAYB"
n = len(s1)
m = len(s2)
print(print_scs_dp(s1, s2))