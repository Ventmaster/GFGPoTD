# 20th July 2024
# Remove Half Nodes

class Solution:
    def RemoveHalfNodes(self, root):
        
        if not root:
            return
        
        root.right = self.RemoveHalfNodes(root.right)
        root.left = self.RemoveHalfNodes(root.left)
        
        if not root.left and not root.right:
            return root
        if root.left and not root.right:
            root = root.left
        if root.right and not root.left:
            root = root.right
        return root
