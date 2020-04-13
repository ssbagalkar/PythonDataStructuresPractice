#https://leetcode.com/problems/3sum/
def find_triplets(arr, n, desired_sum):
    arr.sort()
    return_arr = []
    for ii in range(n - 1):
        start_index = ii + 1
        end_index = n - 1

        while start_index < end_index:
            current_sum = arr[ii] + arr[start_index] + arr[end_index]

            if current_sum > desired_sum:
                start_index += 1
            elif current_sum < desired_sum:
                end_index -= 1
            else:
                return_arr.append([arr[ii], arr[start_index], arr[end_index]])
                start_index+=1
                end_index-=1
    return return_arr


arr = [0, -1, 2, -3, 1]
desired_sum = -2
n = len(arr)
print(find_triplets(arr, n, desired_sum))