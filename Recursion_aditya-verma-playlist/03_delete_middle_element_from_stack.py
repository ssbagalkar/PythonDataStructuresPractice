"""
video --> https://www.youtube.com/watch?v=oCcUNRMl7dA&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=8&ab_channel=AdityaVermaAdityaVerma
"""

def del_middle_element(arr, middle_el_index):
	# base condition
	if middle_el_index == 0:
		arr.pop()
		return arr

	# store temporary values to add later
	tmp = arr.pop()
	del_middle_element(arr, middle_el_index-1)
	arr.append(tmp)
	return arr


array = [5, 4, 3, 2, 1]
middle_index = len(array)//2
print(del_middle_element(array, middle_index))
