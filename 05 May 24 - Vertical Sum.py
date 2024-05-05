# 05 May 2024
# Vertical Sum

class Solution:
    #Complete the function below
    def verticalSum(self, root):
        #:param root: root of the given tree.
        #code here
        d = {}
        
        def func(root, pos = 0):
            if root == None:
                return None
                
            if pos not in d:
                d[pos] = root.data
            else:
                d[pos] += root.data
                
            func(root.left, pos-1), func(root.right, pos+1)
            return d
            
        func(root)
        
        array = []
        
        for x in sorted(d.keys()):
            array.append(d[x])
            
        return array
