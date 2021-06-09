"""
Video Link --> https://www.youtube.com/watch?v=1cspuQ6qHW0&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=14&ab_channel=AdityaVermaAdityaVerma
"""


def permutation_with_spaces(input_string, output_string):
	if input_string == "":
		print(output_string)
		return
	output_string_one = output_string + input_string[0]
	output_string_two = output_string + " " + input_string[0]
	permutation_with_spaces(input_string[1:], output_string_one)
	permutation_with_spaces(input_string[1:], output_string_two)


# driver
permutation_with_spaces("BC", "A")
