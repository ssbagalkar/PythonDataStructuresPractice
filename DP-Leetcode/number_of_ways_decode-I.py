"""
Link --> https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/
Leetcode link --> https://leetcode.com/explore/interview/card/facebook/55/dynamic-programming-3/264/

Complexity    Time       Space
Recursive     O(2^n)     O(1)
DP            0(n)       0(n)

DP solution passes all tests on Leetcode!
"""

def num_decodings(s: str) -> int:
	if len(s) == 0 or (len(s) == 1 and s[0] == '0'):
		return 0
	return num_decodings_helper(s, len(s), 0)


## This recursive solution gives wring answer for "1201234" edge case.The DP approach works though
def num_decodings_helper(s: str, n: int, count) -> int:
	if n == 0 or n == 1:
		return 1
	if s[n - 1] > "0":
		count = num_decodings_helper(s, n - 1, count)
	if s[n - 2] == "1" or (s[n - 2] == "2" and s[n - 1] < "7"):
		count += num_decodings_helper(s, n - 2, count)
	return count


def num_decoding_tabular(s):
	n = len(s)
	if n == 0:
		return 0
	if s[0] == "0":
		return 0
	table = [0] * (n+1)
	table[0] = 1
	table[1] = 1
	for ii in range(2, n+1):
		if s[ii-1] > "0":
			table[ii] = table[ii-1]
		if s[ii-2] == "1" or (s[ii-2] == "2" and s[ii-1] < "7"):
			table[ii] += table[ii-2]
	return table[-1]


# edge cases
# print(num_decodings("1201234")) -- expected 3 , got 7
# print(num_decoding_tabular("1201234")) got 3, right!!
print(num_decodings("226"))
print(num_decoding_tabular("226"))
