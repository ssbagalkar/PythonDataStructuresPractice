
"""
Remove duplicates from sorted array
https://www.youtube.com/watch?v=gf7vdIin0dk
"""

#
# # Extra space
# def remove_duplicates(arr):
#     if len(arr) < 2:
#         return arr
#     jj = 0
#     temp = []
#     for ii in range(len(arr)-1):
#         if arr[ii+1] != arr[ii]:
#             temp.append(arr[ii])
#             jj+=1
#     temp.append(arr[-1])
#     return temp
#
#
# arr = [1,2,2,3,4,4,4]
# print(remove_duplicates(arr))
# arr = [1]                #[1]
# print(remove_duplicates(arr))
# arr = [1, 2, 3]          #[1,2,3]
# print(remove_duplicates(arr))
# arr = [1,1,2,3,3,3]      # [1,2,3]
# print(remove_duplicates(arr))

#GeeksForGeeks
def remove_duplicates_in_place(arr, n):
    if n == 0 or n == 1:
        return n

        # To store index of next
    # unique element
    j = 0

    # Doing same as done
    # in Method 1 Just
    # maintaining another
    # updated index i.e. j
    for i in range(0, n - 1):
        if arr[i] != arr[i + 1]:
            arr[j] = arr[i]
            j += 1

    arr[j] = arr[n - 1]
    j += 1
    return j


# Driver code
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
n = len(arr)

# removeDuplicates() returns
# new size of array.
print(remove_duplicates_in_place(arr, n))


