# 05th August 2024
# Bottom View of Binary Tree

from collections import deque

class Solution:
    def bottomView(self, root):
        # code here
        result = deque([(root.data, 0)])
        left_bound, right_bound = 0, 0
        
        if root == None:
            return result
            
        def traverse(node, d, p):
            nonlocal result, left_bound, right_bound
            
            if node == None:
                return
            
            if p < left_bound:
                left_bound = p
                result.appendleft((node.data, d))
                
            elif p > right_bound:
                right_bound = p
                result.append((node.data, d))
                
            elif result[p - left_bound][1] <= d:
                result[p - left_bound] = (node.data, d)
                
            traverse(node.left, d + 1, p - 1)
            traverse(node.right, d + 1, p + 1)
            
        traverse(root, 0, 0)
        
        return [i[0] for i in result]
