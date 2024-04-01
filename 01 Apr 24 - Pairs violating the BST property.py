# 01 April 2024
# Pairs violating the BST property

class Solution:
    def pairsViolatingBST(self, n : int, root : Optional['Node']) -> int:
        # code here
        list_inorder = []
        
        def inorder(root):
            if not root:
                return 
            
            inorder(root.left)
            list_inorder.append(root.data)
            inorder(root.right)
            
        inorder(root)
        
        if len(list_inorder) <= 1:
            return 0
            
        new_li = []
        for i, val in enumerate(list_inorder):
            new_li.append((val, i))
            
        new_li.sort()
        
        result = 0
        x = []
        
        while new_li:
            val, i = new_li.pop(0)
            count = bisect_right(x, i)
            result += i - count
            x.insert(count, i)
            
        return result
