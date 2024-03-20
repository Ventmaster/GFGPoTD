# 20 March 2024
# Sum of nodes on the longest path from root to leaf node

def f(root,height,temp):
    if root == None:
        return height,temp
        
    left,sum1 = f(root.left,height + 1,temp + root.data)
    right,sum2 = f(root.right,height + 1,temp + root.data)
    
    if left == right:
        if sum1 > sum2:
            return left,sum1
        return right,sum2
    
    if left > right:
        return left,sum1    
    return right,sum2


class Solution:
    def sumOfLongRootToLeafPath(self,root):
        #code here
        
        return f(root,0,0)[1]
