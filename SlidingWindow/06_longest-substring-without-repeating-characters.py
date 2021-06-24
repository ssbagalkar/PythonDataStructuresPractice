"""
Video --> https://www.youtube.com/watch?v=L6cffskouPQ&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=11&ab_channel=AdityaVerma
Leetcode problem link --> https://leetcode.com/problems/longest-substring-without-repeating-characters/

Verified on Leetcode: Yes. No TLE !!

"""


def length_of_longest_substring(s: str) -> int:
	if len(s) == 0:
		return 0

	if len(set(s)) == len(s):
		return len(s)

	data_dict = dict()
	ii = 0
	jj = 0
	output = float("-inf")
	m = len(s)
	while jj < m:
		letter = s[jj]
		if letter in data_dict:
			data_dict[letter] += 1
		else:
			data_dict[letter] = 1

		n = len(data_dict)

		current_count = data_dict[letter]
		if current_count == 1:
			output = max(output, n)
			jj += 1

		elif current_count > 1:
			while n and data_dict[letter] > 1:
				data_dict[s[ii]] -= 1
				if data_dict[s[ii]] <= 0:
					del data_dict[s[ii]]
				ii += 1
				n = len(data_dict)
			jj += 1
	return output


print(length_of_longest_substring("abcabcbb"))