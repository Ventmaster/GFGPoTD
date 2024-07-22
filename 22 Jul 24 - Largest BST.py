# 22nd July 2024
# Largest BST

class Solution:
    def largestBst(self, root):
        # Your code here
        def func(node):
            if not node:
                return True, 0, float('inf'), float('-inf')
                
            left, l_size, l_min, l_max = func(node.left)
            right, r_size, r_min, r_max = func(node.right)
            
            if left and right and l_max < node.data < r_min:
                return True, 1 + l_size + r_size, min(l_min, node.data), max(node.data, r_max)
                
            return False, max(l_size, r_size), 0, 0

        return func(root)[1]
