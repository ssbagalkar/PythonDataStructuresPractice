# https://www.youtube.com/watch?v=SqA0o-DGmEw&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=41&ab_channel=AdityaVermaAdityaVerma
# https://www.geeksforgeeks.org/check-if-a-string-is-a-scrambled-form-of-another-string/

"""
Note: All scrambled versions of each other are anagrams but not all anagrams are scrambled versions of each other
e.g : coder and ocder are scrambled
but abcde and caebd are NOT


Note: This Recursive Solution passes all test cases in InterViewBit!!
I need to figure out a better, more optimized solution i.e memoized either with a dictionary approach or matrix
"""


def is_scrambled_string(s1, s2):
	# differing lengths dont make scrambled string
	if len(s1) != len(s2):
		return False

	n = len(s1)

	# if strings are empty, they are scrambled strings of each other
	if n == 0:
		return True

	# same strings are scrambled versions of each other
	if s1 == s2:
		return True

	# if both strings are NOT anagrams of each other, they are not even scrambled
	if sorted(s1) != sorted(s2):
		return False

	# Follow the conditions given in the video and GeeksForGeeks
	"""
	Given two strings of equal length (say n+1), S1[0…n] and S2[0…n]. If S2 is a scrambled form of S1, 
	then there must exist an index i such that at least one of the following conditions is true: 
	S2[0…i] is a scrambled string of S1[0…i] and S2[i+1…n] is a scrambled string of S1[i+1…n].
	S2[0…i] is a scrambled string of S1[n-i…n] and S2[i+1…n] is a scrambled string of S1[0…n-i-1].
	"""

	for ii in range(1, n):
		if is_scrambled_string(s1[:ii], s2[:ii]) and is_scrambled_string(s1[ii:], s2[ii:]):
			return True
		# can be also written as if is_scrambled_string(s1[n-ii:], s2[:ii]) and is_scrambled_string(s1[:n-ii], s2[ii:]):
		if is_scrambled_string(s1[-ii:], s2[:ii]) and is_scrambled_string(s1[:-ii], s2[ii:]):
			return True
	return False


# Test cases
s1 = "great"
s2 = "eatgr"
memo = [[False for _ in range(len(s1))] for _ in range(len(s2))]
print(is_scrambled_string(s1, s2))  # expected True

s1 = "abcde"
s2 = "caebd"
print(is_scrambled_string(s1, s2))  # expected False
