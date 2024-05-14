# 14th May 2024
# Path With Minimum Effort

from typing import List

class Solution:
    def MinimumEffort(self, rows : int, columns : int, heights : List[List[int]]) -> int:
        # code here
        def dfs(middle):
            stack = [(0,0)]
            visited = set()
            
            while stack:
                x, y = stack.pop()
                
                if x == rows - 1 and y == columns-1:
                    return True
                    
                visited.add((x,y))
                
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < rows and 0 <= ny < columns and (nx, ny) not in visited and abs(heights[nx][ny] - heights[x][y]) <= middle:
                        stack.append((nx, ny))
            return False
            
        left, right, result = 0, int(1e6), float('inf')
        
        while left <= right:
            middle = (left + right) // 2
            
            if dfs(middle):
                result, right = middle, middle - 1
            else:
                left = middle + 1
                
        return result
