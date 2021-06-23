"""
https://www.geeksforgeeks.org/count-occurrences-of-anagrams/

Complexity:
Method                            Time (worst)     Auxiliary Space(worst)   Passing tests?
Not optimized                       O(n*k)           O(k)                     Yes, with TLE
Optimized                           O(n)             O(k)                     No, failing for few
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


def count_number_of_anagrams_optimized(my_string, my_pattern):
	if len(my_string) == 0 or len(my_pattern) == 0:
		return 0
	n = len(my_string)
	k = len(my_pattern)

	if len(my_pattern) > len(my_string):
		return 0

	count = 0
	if len(my_pattern) == 1:
		for char in my_string:
			if char == my_pattern:
				count+=1
		return count


	deq = deque()
	count_dict = dict()
	for letter in my_pattern:
		if letter in count_dict:
			count_dict[letter] += 1
		else:
			count_dict[letter] = 1

	for ii in range(k):
		letter = my_string[ii]
		if letter in count_dict:
			count_dict[letter] -= 1
	values = [value for key, value in count_dict.items()]
	if any(values) is False:
		count += 1
	deq.append(my_string[0])
	for ii in range(1, n-k+1):
		to_remove = deq[0]
		if to_remove in count_dict:
			count_dict[to_remove] -= 1
		deq.popleft()
		to_include = my_string[ii]
		deq.append(to_include)

		if to_include in count_dict:
			count_dict[to_include] += 1

		values = [value for key, value in count_dict.items()]
		if any(values) is False:
			count += 1
	return count


# big_string = "aabaabaa"
# small_string = "aaba"
# big_string = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
# small_string = "kkkkk"
big_string = "wbgjb"
small_string = "b"
print(count_number_of_anagrams_brute(big_string, small_string))
print(count_number_of_anagrams_optimized(big_string, small_string))
