arr = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]

## Soln 1 ( uses operator and sort functions)
#import operator

# def most_frequent(arr):
#     count_dict = {}
#     if len(arr)>0:
#         for ii in range(len(arr)):
#             if arr[ii] in count_dict:
#                 count_dict[arr[ii]]+=1
#             else:
#                 count_dict[arr[ii]] = 1
#         sorted_by_values = sorted(count_dict.items(), key=operator.itemgetter(1))
#         most_frequent_item = sorted_by_values[-1][0]
#         return most_frequent_item

## Better and elegant solution
def most_frequent(arr):
	max_count = -1
	max_element = None
	count_dict = {}
	for item in arr :
		if item in count_dict:
			count_dict[item]+=1
		else:
			count_dict[item] = 1

		if count_dict[item] > max_count:
			max_count = count_dict[item]
			max_element = item
	return max_element




print(most_frequent(arr))