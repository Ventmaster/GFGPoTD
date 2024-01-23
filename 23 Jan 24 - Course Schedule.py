# 23 January 2024
# Course Schedule

from collections import defaultdict

class Solution:
    def findOrder(self, n, m, prerequisites):
        # Code here
        graph = defaultdict(list)
            
        for a, b in prerequisites:
            graph[a].append(b)
            
        result, visited = [], [0] * n
        
        def dfs(i):
            if visited[i]:
                return visited[i]==1
            visited[i] = -1 
            
            if any (not dfs(node) for node in graph[i]):
                return False
                
            visited[i] = 1
            
            result.append(i)
            
            return True
            
        return all(dfs(node) for node in range(n)) and result or []
