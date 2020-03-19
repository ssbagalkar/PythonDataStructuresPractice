
"""
Remove duplicates from sorted array
https://www.youtube.com/watch?v=gf7vdIin0dk
"""


# Extra space
def remove_duplicates(arr):
    if len(arr) < 2:
        return arr
    jj = 0
    temp = []
    for ii in range(len(arr)-1):
        if arr[ii+1] != arr[ii]:
            temp.append(arr[ii])
            jj+=1
    temp.append(arr[-1])
    return temp


arr = [1,2,2,3,4,4,4]
print(remove_duplicates(arr))
arr = [1]                #[1]
print(remove_duplicates(arr))
arr = [1, 2, 3]          #[1,2,3]
print(remove_duplicates(arr))
arr = [1,1,2,3,3,3]      # [1,2,3]
print(remove_duplicates(arr))

