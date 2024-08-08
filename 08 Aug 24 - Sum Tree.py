# 08th August 2024
# Sum Tree

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def is_sum_tree(self, node):
        return self.func(node) != -1
    
    def func(self, node):
        # code here
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return node.data
            
        left_sum = self.func(node.left)
        right_sum = self.func(node.right)
        
        if left_sum == -1 or right_sum == -1 or (left_sum + right_sum != node.data):
            return -1
            
        return left_sum + right_sum + node.data
