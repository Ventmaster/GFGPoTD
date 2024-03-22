# 22 March 2024
# Diagonal sum in binary tree

from collections import defaultdict

class Solution:
    def diagonalSum(self, root):
        d=defaultdict(int)
        
        def helper(root, slope):
            if(root is not None):
                d[slope] += root.data
                helper(root.left, slope+1)
                helper(root.right, slope)
        
        helper(root, 0)
        
        res=[]
        n=len(d)
        
        for i in range(n):
            res.append(d[i])
        return res
