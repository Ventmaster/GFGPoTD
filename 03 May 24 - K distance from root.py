# 03 May 2024
# K distance from root

from collections import deque

class Solution:
    def KDistance(self,root,k):
        # code here
        if not root:
            return []
            
        queue = deque()
        queue.append((root, 0))
        q = list()
        
        while queue:
            if (queue[0][1] == k):
                q.append(queue[0][0].data)
            node = queue.popleft()
            
            if (node[0].left):
                queue.append((node[0].left, node[1] + 1))
            if (node[0].right):
                queue.append((node[0].right, node[1] + 1))
                
        return q
