"""
Link --> https://www.youtube.com/watch?v=eyCj_u3PoJE&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=18&ab_channel=AdityaVerma
"""


def generate_all_balanced_parantheses(open_count, close_count, output_str):
	# base condition
	if open_count <= 0 and close_count <= 0:
		print(output_str)
		return

	if close_count > open_count:
		if open_count > 0:
			generate_all_balanced_parantheses(open_count-1, close_count, output_str+'(')
		if close_count > 0:
			generate_all_balanced_parantheses(open_count, close_count-1, output_str+')')
	else:
		generate_all_balanced_parantheses(open_count-1, close_count, output_str+'(')


# driver
n = 3
open_count = n
close_count = n
output_str = ""
generate_all_balanced_parantheses(open_count, close_count, output_str)
