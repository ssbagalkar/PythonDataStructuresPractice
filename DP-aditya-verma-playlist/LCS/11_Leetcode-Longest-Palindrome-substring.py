"""
Problem statement: https://leetcode.com/problems/longest-palindromic-substring/
Solution explained: https://www.youtube.com/watch?v=y2BD4MJqV20&ab_channel=NickWhite
Passed all tests--> Yess!!!
Complexity -- Time-> 0(n^2)
				Space --> O(1)
"""

def get_longest_palindrome_recursive(s):
	n = len(s)
	if n == 0:
		return ""
	if n == 1:
		return s

	start = 0
	end = 0
	for ii in range(n):
		len_one = expand_from_middle(s, ii, ii)
		len_two = expand_from_middle(s, ii, ii+1)
		length = max(len_one, len_two)
		if length > (end - start):
			start = ii - length//2
			end = ii + length//2
	return s[start:end+1]


def expand_from_middle(s, left, right):
	if len(s) == 0 or left > right: return ""
	n = len(s)

	while left >= 0 and right < n and s[left] == s[right]:
		left -= 1
		right += 1
	return right-left-1


print(get_longest_palindrome_recursive("cbbd"))
