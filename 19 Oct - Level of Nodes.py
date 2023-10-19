# 19 October 2023
# Level of Nodes

class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here
        level = 0
        visited = [False] * V
        queue = [0]
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.pop(0)
                
                if node == X:
                    return level
                    
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            level = level + 1
            
        return -1 
