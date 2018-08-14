"""The following implementation assumes that the activities
are already sorted according to their finish time"""
 
"""Prints a maximum set of activities that can be done by a
single person, one at a time"""
# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities

## https://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/
 
def printMaxActivities(s , f ):
    n = len(f)
    print ("The following activities are selected")
 
    # The first activity is always selected
    i = 0
    print (i,end=" ")
 
    # Consider rest of the activities
    for j in range(n):
 
        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            print (j,end=" ")
            i = j
 
# Driver program to test above function
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
printMaxActivities(s , f)