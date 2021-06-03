"""
https://www.youtube.com/watch?v=5P84A0YCo_Y&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=10&ab_channel=AdityaVermaAdityaVerma

Lettcode Problem Link--> https://leetcode.com/problems/k-th-symbol-in-grammar/

Checked om Leetcode: Yes
Did it pass all use cases -->  Yes!!
"""


def find_kth_element(n, k):
	# base condition
	if n == 1 and k == 1:
		return 0

	mid_idx = 2 ** (n - 1) // 2
	if k <= mid_idx:
		return find_kth_element(n - 1, k)
	return int(not find_kth_element(n - 1, k - mid_idx))


print(find_kth_element(4, 7))
