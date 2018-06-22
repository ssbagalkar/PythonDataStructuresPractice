# Implement your function below.
def common_elements(arr_1, arr_2):
    common_element_list = []
    ii = jj = 0
    while ( ii < len(arr_1) and jj < len(arr_2) ):
        if arr_1[ii] == arr_2[jj]:
            common_element_list.append(arr_1[ii])
            ii+=1
        else:
            if arr_1[ii] < arr_2[jj]:
                ii+=1
            else:
                jj+=1
    return common_element_list


# NOTE: The following input values will be used for testing your solution.
list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
# common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
# common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).