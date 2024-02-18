# 18 February 2024
# Sum of leaf nodes in BST

class Solution:
    def sumOfLeafNodes(self, root):
        #Your code here
        def dfs(node):
            nonlocal result
            
            if not node:
                return
            
            if not node.left and not node.right:
                result += node.data
                
            dfs(node.left)
            dfs(node.right)
            
        result = 0
        dfs(root)
        
        return result
