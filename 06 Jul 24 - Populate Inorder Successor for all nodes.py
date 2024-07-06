# 06th July 2024
# Populate Inorder Successor for all nodes

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None

class Solution:
    def populateNext(self, root):
        def inorder(node):
            nonlocal previous
            
            if not node:
                return
            
            inorder(node.left)
            
            if previous is not None:
                previous.next = node
                
            previous = node
            
            inorder(node.right)
            
        previous = None
        
        inorder(root)
