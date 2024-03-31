# 31 March 2024
# Closest Neighbour in BST

class Solution:
    def findMaxForN(self, root, n):
        #Print the value of the element if it exists otherwise print -1.
        #code here
        result = None
        
        while root:
            if root.key > n:
                root = root.left
            else:
                result = root.key
                root = root.right
                
        return result if result else -1
