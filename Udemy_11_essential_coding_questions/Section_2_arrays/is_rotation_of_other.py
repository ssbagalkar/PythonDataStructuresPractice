# Solution from lesson
# Small and efficient one
def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    key = list1[0]
    key_loc = -1
    for i in range(len(list2)):
        if list2[i] == key:
            key_loc = i
            break
    if key_loc == -1:
        return False
    for i in range(len(list1)):
        j = (key_loc + i) % len(list1)
        if list1[i] != list2[j]:
            return False
    return True
		
## My solution. This also works but is not clean and efficient
# def is_rotation(my_array_one, my_array_two):
	# ii = 0
	# jj = 0
	# found = False
	# if len(my_array_one) != len(my_array_two):
		# return False
	
	# while (ii < len(my_array_one)):
		# if my_array_one[ii] == my_array_two[0]:
			# found = True
			# break
		# else:
			# ii += 1
	
	# if found:
		# jj += 1
		# for mm in range(ii + 1, len(my_array_one)):
			# if my_array_one[mm] != my_array_two[jj]:
				# return False
			# jj += 1
	
	# ii = 0
	# for kk in range(jj, len(my_array_two)):
		# if my_array_two[kk] != my_array_one[ii]:
			# return False
		# ii += 1
	# return True

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
