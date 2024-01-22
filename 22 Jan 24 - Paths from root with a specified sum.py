# 22 January 2024
# Paths from root with a specified sum

from collections import deque

class Solution:
    def printPaths(self, root, sum):
        #code here
        if not root:
            return []
            
        queue, result = deque(), []
        queue.append([root, root.data, [root.data]])
        
        while queue:
            current_node, current_sum, current_route = queue.popleft()
            
            if current_sum == sum:
                result.append(current_route[:])
                
            if current_node.left:
                left_child = current_node.left
                queue.append([left_child, current_sum + left_child.data, current_route + [left_child.data]])
                
            if current_node.right:
                right_child = current_node.right
                queue.append([right_child, current_sum + right_child.data, current_route + [right_child.data]])
                
        return result
