"""
Video Link -->  https://www.youtube.com/watch?v=lfFqW1DTsqM&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=13&ab_channel=AdityaVermaAdityaVerma

"""


def get_unique_subsets(input_str, output, my_set):
	# base condition
	if input_str == "":
		my_set.add(output)
		return

	output_one = output
	output_two = output + input_str[0]
	get_unique_subsets(input_str[1:], output_one, my_set)
	get_unique_subsets(input_str[1:], output_two, my_set)
	return my_set


print(get_unique_subsets(input_str="aab", output="", my_set=set()))
