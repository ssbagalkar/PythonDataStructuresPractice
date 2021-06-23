"""
Video Link --> https://www.youtube.com/watch?v=Lav6St0W_pQ&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=10&ab_channel=AdityaVerma
Problem Link --> https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

Verified on Geeks and Passed all tests without TLE

The general pattern is for such problems is given in the video.
"""



def longest_k_substr(s, k):
	if k > len(s):
		return -1
	if k > len(set(s)):
		return -1
	output = float("-inf")
	ii = 0
	jj = 0
	data_dict = dict()
	map_size = 0
	n = len(s)
	while jj < n:
		letter = s[jj]
		if letter not in data_dict:
			map_size += 1
			data_dict[letter] = 1
		else:
			data_dict[letter] += 1

		if map_size < k:
			jj += 1

		elif map_size == k:
			length_of_substring = sum([v for k, v in data_dict.items()])
			output = max(output, length_of_substring)
			jj += 1
		else:
			while map_size > k:
				char_to_remove = s[ii]
				if data_dict[char_to_remove] <= 1:
					del data_dict[char_to_remove]
					map_size -= 1
				else:
					data_dict[char_to_remove] -= 1
				ii += 1
			jj += 1
	return output

s = "aabacbebebe"
k = 3
print(longest_k_substr(s, k))