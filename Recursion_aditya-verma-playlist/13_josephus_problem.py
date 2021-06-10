"""
Link-->https://www.youtube.com/watch?v=ULUNeD0N9yI&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=19&ab_channel=AdityaVermaAdityaVerma
"""


def josephus_death_problem(arr, k, n, index):

	# base condition
	if n == 1:
		return arr[0]

	index = (index + k) % n
	return josephus_death_problem(arr[:index]+arr[index+1:], k, n-1, index)

#driver
n = 5
k = 2
print(josephus_death_problem([ii for ii in range(1, n+1)], k-1, n, 0))