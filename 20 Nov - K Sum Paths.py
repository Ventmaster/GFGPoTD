# 20 November 2023
# K Sum Paths

class Solution:
    def find_subtree_sum_paths(self, node, target_sum, current_sum, sum_frequency):
        if not node:
            return 
        
        current_sum = current_sum + node.data
        self.path_count += sum_frequency.get(current_sum - target_sum, 0)
        sum_frequency[current_sum] = sum_frequency.get(current_sum, 0) + 1
        
        self.find_subtree_sum_paths(node.left, target_sum, current_sum, sum_frequency)
        self.find_subtree_sum_paths(node.right, target_sum, current_sum, sum_frequency)
        
        sum_frequency[current_sum] -= 1
        
    def sumK(self,root,target_sum):
        # code here
        self.path_count = 0
        current_sum = 0
        sum_frequency = {0: 1}
        
        self.find_subtree_sum_paths(root, target_sum, current_sum, sum_frequency)
        
        return self.path_count
