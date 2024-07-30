# 30th July 2024
# Rat in a Maze Problem - I

from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        n = len(m)
        result = []
        
        if m[0][0] == 0 or m[n-1][n-1] == 0:
            return []
            
        def dfs(x, y, path, result):
            if x == n - 1 and y == n - 1:
                result.append(path)
                return 
            
            m[x][y] = 0
            directions = [('D',1,0),('L',0,-1),('R',0,1),('U',-1,0)]
            
            for dir in directions:
                move, dx, dy = dir
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n and m[nx][ny] == 1:
                    dfs(nx, ny, path + move, result)
            
            m[x][y] = 1
            
        dfs(0, 0, '', result)
        
        return sorted(result)
