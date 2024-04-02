# 02 April 2024
# Minimum Absolute Difference in BST

class Solution:
    def traverse(self, root):
        if root == None:
            return
        
        if root.left != None:
            self.traverse(root.left)
        
        self.nodes.append(root.data)
        
        if root.right != None:
            self.traverse(root.right)
            
        return root.data
    
    def absolute_diff(self, root):
        # Your code here
        self.mad = 10**9 
        self.nodes = []
        
        self.traverse(root)
        
        for i in range(1, len(self.nodes)):
            self.mad = min(self.mad, self.nodes[i] - self.nodes[i-1])
            
        return self.mad
