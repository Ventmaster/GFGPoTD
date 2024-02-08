# 08 February 2024
# Check if all leaves are at same level

class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        #Code here
        result = []
        
        def func(root, level):
            if not root:
                return
            elif not root.left and not root.right:
                result.append(level)
                
            func(root.left, level+1)
            func(root.right, level+1)
            
        func(root, 0)
        
        return len(set(result)) == 1
