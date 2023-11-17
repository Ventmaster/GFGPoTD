# 17 November 2023
# Binary Tree to CDLL

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

'''

class Solution:
    
    #Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        #Your code here
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            
            if not self.previous_node:
                self.head = self.previous_node = node
            else:
                self.previous_node.right, node.left = node, self.previous_node
                
            self.previous_node = node
            inorder_traversal(node.right)
            
        self.head = self.previous_node = None
        
        inorder_traversal(root)
        
        self.head.left, self.previous_node.right = self.previous_node, self.head
        
        return self.head
