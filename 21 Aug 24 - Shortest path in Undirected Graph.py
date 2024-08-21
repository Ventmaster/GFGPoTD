# 21st August 2024
# Shortest path in Undirected Graph

from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        # 📒 Step 1: Create the adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # Because the graph is undirected
        
        # 🚥 Step 2: Prepare for BFS
        dist = [-1] * n  # Distance to all nodes initialized to -1
        dist[src] = 0    # Distance to source is 0
        queue = deque([src])
        
        # 🏃‍♂️ Step 3: BFS
        while queue:
            node = queue.popleft()
            current_dist = dist[node]
            
            for neighbor in graph[node]:
                if dist[neighbor] == -1:  # If neighbor has not been visited
                    dist[neighbor] = current_dist + 1
                    queue.append(neighbor)
        
        # 🎉 Step 4: Return the distances
        return dist
