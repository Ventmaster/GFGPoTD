# 07 February 2024
# Min distance between two given nodes of a Binary Tree

class Solution:
    def findDist(self,root,a,b):
        def dist_to_node(node, target):
            if not node:
                return -1
            if node.data == target:
                return 0
                
            l = dist_to_node(node.left, target)
            r = dist_to_node(node.right, target)
            
            if l >= 0:
                return l+1
            if r >= 0:
                return r+1 
                
            return -1 
            
        def func(node, a, b):
            if not node:
                return None
            
            if node.data == a or node.data == b:
                return node
                
            left = func(node.left, a, b)
            right = func(node.right, a, b)
            
            if left and right:
                return node
            return left if left else right
            
        func_node = func(root, a, b)
        
        return dist_to_node(func_node, a) + dist_to_node(func_node, b)
