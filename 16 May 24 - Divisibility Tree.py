# 16th May 2024
# Divisibility Tree

from typing import List

class Solution:
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        # code here
        def dfs(node, parent, adjacent, subtree_size, removable_edges):
            count = 1
            
            for neighbour in adjacent[node]:
                if neighbour != parent:
                    count = count + dfs(neighbour, node, adjacent, subtree_size, removable_edges)
            
            subtree_size[node] = count
            
            if count % 2 == 0 and node != 1:
                removable_edges.append((parent, node))
            
            return count
            
        adjacent = {i: [] for i in range(1,n+1)}
        
        for u, v in edges:
            adjacent[u].append(v)
            adjacent[v].append(u)
            
        subtree_size = [0] * (n + 1)
        removable_edges = []
        
        dfs(1, -1, adjacent, subtree_size, removable_edges)
        
        return len(removable_edges)
