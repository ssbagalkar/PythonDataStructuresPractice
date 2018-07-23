def most_common(my_array_one, my_array_two):
	ii = 0
	jj = 0
	common_array=[]
	while(ii<len(my_array_one) and jj<len(my_array_two)):
		if my_array_one[ii] == my_array_two[jj]:
			common_array.append(my_array_one[ii])
			ii+=1
			jj+=1
		elif my_array_one[ii] > my_array_two[jj]:
			jj+=1
		else:
			ii+=1
	if common_array:	
		return common_array
	return None
			

my_array_one = [1, 3, 4, 6, 7, 9]
my_array_two = [1, 2, 4, 5, 9, 10]

print(most_common(my_array_one,my_array_two))