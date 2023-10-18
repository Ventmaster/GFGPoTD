# 18 October 2023
# Eventual Safe States

from typing import List

def has_cycle(u, adjacency_list, visited, in_current_stack, nodes_in_cycle):
    visited[u] = 1
    in_current_stack[u] = 1
    
    for v in adjacency_list[u]:
        if not visited[v]:
            if has_cycle(v, adjacency_list, visited, in_current_stack, nodes_in_cycle):
                nodes_in_cycle[u] = 1
                return 1 
        elif in_current_stack[v]:
            nodes_in_cycle[u] = 1
            return 1 
            
    in_current_stack[u] = False
    return False

class Solution:    
    def eventualSafeNodes(self, V : int, adjacency_list : List[List[int]]) -> List[int]:
        # code here
        safe_nodes = []
        visited = [0] * V
        in_current_stack = [0] * V
        nodes_in_cycle = [0] * V
        
        for i in range(V):
            if not visited[i]:
                has_cycle(i, adjacency_list, visited, in_current_stack, nodes_in_cycle)
                
        return [i for i in range(V) if not nodes_in_cycle[i]]
