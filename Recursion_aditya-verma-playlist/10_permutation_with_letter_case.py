"""
https://www.youtube.com/watch?v=J2Er5XceU_I&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=15&ab_channel=AdityaVermaAdityaVerma
"""
def permutation_with_letter_change(input_str, output_str):
	# base condition
	if len(input_str) == 0:
		print(output_str)
		return

	# logic
	if not input_str[0].isdigit():
		permutation_with_letter_change(input_str[1:], output_str + input_str[0].lower())
		permutation_with_letter_change(input_str[1:], output_str + input_str[0].upper())
	else:
		permutation_with_letter_change(input_str[1:], output_str + input_str[0])

#driver
input_str = "a1b2"
permutation_with_letter_change(input_str, "")