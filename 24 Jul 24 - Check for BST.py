# 24th July 2024
# Check for BST

class Solution:
    def func(self, node, min_val, max_val):
        if node is None:
            return True
            
        if not(min_val < node.data < max_val):
            return False
            
        return self.func(node.left, min_val, node.data) and self.func(node.right, node.data, max_val)
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        return self.func(root, float('-inf'), float('inf'))
