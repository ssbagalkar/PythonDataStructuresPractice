"""
Video Link --> https://www.youtube.com/watch?v=Yg5a2FxU4Fo&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=12&ab_channel=AdityaVermaAdityaVerma
Geeks link -->  https://practice.geeksforgeeks.org/problems/power-set-using-recursion/1/?track=sp-recursion&batchId=105
Time complexity -- > O(2^N)
Space Complexity --> ?
"""


def generate_power_set(input_str, output):
	# base condition
	if input_str == "":
		print(output)
		return

	output_one = output
	output_two = output + input_str[0]
	generate_power_set(input_str[1:], output_one)
	generate_power_set(input_str[1:], output_two)


# driver code
generate_power_set("abc", "")
