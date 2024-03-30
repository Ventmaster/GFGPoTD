# 30 March 2024
# Minimum element in BST

class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        ##Your code here
        while root.left:
            root = root.left
            
        return root.data
