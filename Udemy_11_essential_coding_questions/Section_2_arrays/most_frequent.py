def most_occuring_item(my_array):
	my_dict=dict()
	n = len(my_array)
	most_occuring=None
	current_count = -1
	max_count = -1
	for item in my_array:
		if item in my_dict:
			my_dict[item]+=1
			current_count = my_dict[item]
			if current_count > max_count:
				max_count = current_count
				most_occuring = item
			
		else:
			my_dict[item] = 1
			
	return most_occuring
	
	
	
	
my_array = [10,1,7,7,7,1,4]	
print(most_occuring_item(my_array))