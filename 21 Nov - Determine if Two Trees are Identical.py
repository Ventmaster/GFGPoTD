# 21 November 2023
# Determine if Two Trees are Identical

#User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here
        if root1 is None and root2 is None:
            return True
            
        elif root1 is None or root2 is None:
            return False
        
        elif root1.data != root2.data:
            return False
            
        left_check = self.isIdentical(root1.left, root2.left)
        right_check = self.isIdentical(root1.right, root2.right)
        
        return left_check and right_check
