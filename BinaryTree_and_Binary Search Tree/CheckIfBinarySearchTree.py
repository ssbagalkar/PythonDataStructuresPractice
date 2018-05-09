# Python program to check if a binary tree is bst or not
 
INT_MAX = 4294967296
INT_MIN = -4294967296
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None