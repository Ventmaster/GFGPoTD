# 02nd September 2024
# Minimum Cost Path

import heapq

class Solution:
    # Function to return the minimum cost to reach the bottom-right cell from the top-left cell.
    def minimumCostPath(self, grid):
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        li = []
        
        heapq.heappush(li, (grid[0][0], 0, 0))
        cost = [[float('inf')] * n for _ in range(n)]
        
        cost[0][0] = grid[0][0]
        
        while li:
            current_cost, x, y = heapq.heappop(li)
            
            if x == n - 1 and y == n - 1:
                return current_cost
                
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = current_cost + grid[nx][ny]
                    
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heapq.heappush(li, (new_cost, nx, ny))
                        
        return cost[n-1][n-1]