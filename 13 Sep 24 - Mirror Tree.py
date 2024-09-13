# 13th September 2024
# Mirror Tree

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        if root is None:
            return 
        
        self.mirror(root.left)
        self.mirror(root.right)
        
        root.left, root.right = root.right, root.left
