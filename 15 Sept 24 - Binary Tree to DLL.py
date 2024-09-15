# 15th September 2024
# Binary Tree to DLL

class Solution:
    def binary_to_dll(self, prev, head, root):
        if root is None:
            return prev, head
            
        prev, head = self.binary_to_dll(prev, head, root.left)
        
        if head is None:
            head = root
            
        else:
            root.left = prev
            
            if prev is not None:
                prev.right = root
                
        prev = root
        
        return self.binary_to_dll(prev, head, root.right)
    
    def bToDLL(self,root):
        # do Code here
        prev, head = self.binary_to_dll(None, None, root)
        
        return head
