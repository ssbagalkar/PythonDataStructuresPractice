#BreadthFirstSearch
#Complexity O(n^2)

# Recursive Python program for level order traversal of Binary Tree
 
# A node structure
class Node:
 
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None
 
