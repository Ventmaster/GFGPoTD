# 22 November 2023
# Symmetric Tree

class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        # Your Code Here
        if not root:
            return True
            
        def func(node1, node2):
            if not node1 and not node2:
                return True
            elif (not node1 or not node2) or (node1.data != node2.data):
                return False
                
            return func(node1.left, node2.right) and func(node1.right, node2.left)
        
        return func(root.left, root.right)
