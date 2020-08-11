"""
Problem Statement:
Evaluate Expression To True-Boolean Parenthesization Recursion
Given a boolean expression with following symbols.
Symbols
    'T' --- true
    'F' --- false
And following operators filled between symbols
Operators
    &   ---boolean AND
    |   --- boolean OR
    ^   --- boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.
Example:
Input: symbol[]    = {T, F, T}
       operator[]  = {^, &}
Output: 2
The given expression is "T ^ F & T", it evaluates true
in two ways "((T ^ F) & T)" and "(T ^ (F & T))"

Youtube link --> https://www.youtube.com/watch?v=pGVguAcWX4g&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=39
Useful link for code - https://www.youtube.com/watch?v=7Gk36fHV38E&t=854s
Geeks Link --> https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/

Complexity:
Time -->
Space -->

Verified in Leetcode/InterviewBits--> No
"""


def solve(s: str, i: int, j: int, is_true: bool):
    if i > j:
        return False
    if i == j:
        if is_true:
            return s[i] == 'T'
        else:
            return s[i] == 'F'

    num_ways = 0

    for k in range(i+1, j, 2):
        left_true = solve(s, i, k-1, is_true=True)
        left_false = solve(s, i, k-1, is_true=False)
        right_true = solve(s, k+1, j, is_true=True)
        right_false = solve(s, k+1, j, is_true=False)

        if s[k] == '&':
            if is_true is True:
                num_ways += left_true * right_true
            else:
                num_ways += (left_false * right_false) + (left_false * right_true) + (left_true * right_false)

        elif s[k] == '|':
            if is_true is True:
                num_ways += (left_false * right_true) + (left_true * right_false) + (left_true * right_true)
            else:
                num_ways += left_false * right_false
        elif s[k] == '^':
            if is_true is True:
                num_ways += (left_false * right_true) + (left_true * right_false)
            else:
                num_ways += (left_false * right_false) + (left_true * right_true)

    return num_ways


my_str = "T|T&F^T"
# my_str = 'T^F&T'
print(solve(my_str, 0, len(my_str)-1, True))
