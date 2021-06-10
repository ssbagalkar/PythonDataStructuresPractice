"""
Link --> https://www.youtube.com/watch?v=U81n0UYtk98&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=18&ab_channel=AdityaVermaAdityaVerma
"""

def print_nth_prefix_binary(n, count_zeros, count_ones, output_string):
	#base condition
	if n == 0:
		print(output_string)
		return

	if len(output_string) > 0:
		if count_zeros < count_ones:
			print_nth_prefix_binary(n - 1, count_zeros, count_ones+1, output_string+"1")
			print_nth_prefix_binary(n - 1, count_zeros+1, count_ones, output_string+"0")
		else:
			print_nth_prefix_binary(n - 1, count_zeros, count_ones + 1, output_string + "1")
	else:
		print_nth_prefix_binary(n-1, count_zeros, count_ones+1, output_string+"1")


# driver
n = 2
print_nth_prefix_binary(n, 0, 0, "")