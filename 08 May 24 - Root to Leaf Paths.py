# 08 May 2024
# Root to Leaf Paths

from typing import Optional
from collections import deque
from typing import List

class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # code here
        result = []
        
        def recursion(node, path):
            if not node:
                return
            
            if not node.left and not node.right:
                result.append(path + [node.data])
                return
            
            if node.left:
                recursion(node.left, path + [node.data])
                
            if node.right:
                recursion(node.right, path + [node.data])
            
        recursion(root, [])
        
        return result
