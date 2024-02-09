# 09 February 2024
# Check for Children Sum Property in a Binary Tree

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        if not root or (not root.left and not root.right):
            return 1
            
        Left, Right, add = 1, 1, 0
        
        if root.left:
            Left = self.isSumProperty(root.left)
            add += root.left.data
        if root.right:
            Right = self.isSumProperty(root.right)
            add += root.right.data
            
        return int(root.data == add) and Left and Right
