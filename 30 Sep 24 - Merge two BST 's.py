# 30th September 2024
# Merge two BST 's

class Solution:
    def merge(self, root1, root2):
        # code here
        li = []
        
        def tree(root, li):
            if root is None:
                return
            
            li.append(root.data)
            
            tree(root.left, li)
            tree(root.right, li)
            
        tree(root1, li)
        tree(root2, li)
        
        li.sort()
        
        return li
