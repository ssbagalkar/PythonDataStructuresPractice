"""
https://www.geeksforgeeks.org/count-occurrences-of-anagrams/

Complexity:
Method                            Time (worst)     Auxiliary Space(worst)   Passing tests?
Not optimized                       O(n*k)           O(k)                     Yes, with TLE
Optimized                           O(n)             O(k)                     Yess!!
"""


import copy
from collections import deque


def count_number_of_anagrams_brute(my_string, my_pattern):
	if len(my_string) == 0 or len(my_pattern) == 0:
		return 0
	n = len(my_string)
	k = len(my_pattern)

	count = 0
	for ii in range(n - k + 1):
		pattern_dict = dict()
		# Build the dictionary everytime
		for letter in my_pattern:
			if letter in pattern_dict:
				pattern_dict[letter] += 1
			else:
				pattern_dict[letter] = 1
		jj = 0
		while jj < k:
			current_letter = my_string[ii + jj]
			if current_letter in pattern_dict:
				pattern_dict[current_letter] -= 1
			jj += 1
		values = [value for key, value in pattern_dict.items()]
		if any(values) is False:
			count += 1
	return count


def count_number_of_anagrams_optimized(str1, str2):
	n = len(str1)
	m = len(str2)
	result = 0
	if m > n or n == 0 or m == 0:
		return 0
	anagram_dict = dict()

	for letter in str2:
		if letter not in anagram_dict:
			anagram_dict[letter] = 1
		else:
			anagram_dict[letter] += 1

	my_dict = dict()
	for letter in str1[:m]:
		if letter not in my_dict:
			my_dict[letter] = 1
		else:
			my_dict[letter] += 1
	if anagram_dict == my_dict:
		result += 1

	for ii in range(m, n):
		to_remove = str1[ii - m]
		to_add = str1[ii]
		if to_remove in my_dict:
			my_dict[to_remove] -= 1
			if my_dict[to_remove] == 0:
				del my_dict[to_remove]
		if to_add not in my_dict:
			my_dict[to_add] = 1
		else:
			my_dict[to_add] += 1
		if my_dict == anagram_dict:
			result += 1
	return result




big_string = "aabaabaa"
small_string = "aaba"
# big_string = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
# small_string = "kkkkk"
# big_string = "wbgjb"
# small_string = "b"
print(count_number_of_anagrams_brute(big_string, small_string))
print(count_number_of_anagrams_optimized(big_string, small_string))
