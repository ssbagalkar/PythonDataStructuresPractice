"""
Youtube link --> https://www.youtube.com/watch?v=l45md3RYX7c&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=11&ab_channel=AdityaVermaAdityaVerma
geeks link --> https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/
Time complexity --> O(2^n)
Space --> O(N)
"""


def tower_of_hanoi(n, source, destination, auxiliary):
	if n == 1:
		print("Move disk 1 from source", source, "to destination", destination)
		return
	tower_of_hanoi(n - 1, source, auxiliary, destination)
	print("Move disk", n, "from source", source, "to destination", destination)
	tower_of_hanoi(n - 1, auxiliary, destination, source)


# Driver code
n = 3
tower_of_hanoi(n, 'A', 'B', 'C') #A is source, B is destination