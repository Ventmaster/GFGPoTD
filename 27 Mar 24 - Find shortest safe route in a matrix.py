# 27 March 2024
# Find shortest safe route in a matrix

from typing import List
from collections import deque

class Solution:
    def __init__(self):
        self.delrow = [-1, 0, 0, 1]
        self.delcol = [0, -1, 1, 0]
    
    def findShortestPath(self, mat : List[List[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])
        q = deque()
        d = [[float('inf')] * m for _ in range(n)]
        
        def valid(i, j):
            return 0 <= i < n and 0 <= j < m
            
        def check(i, j):
            if not valid(i, j):
                return False
            for k in range(4):
                if valid(i + self.delrow[k], j + self.delcol[k]) and mat[i + self.delrow[k]][j+self.delcol[k]]==0:
                    return False
            return True
            
        for i in range(n):
            if check(i, m-1):
                q.append((i, m-1, 1))
        
        while q:
            x, y, dis = q.popleft()
            
            if d[x][y] > dis:
                d[x][y] = dis
                
                for k in range(4):
                    if check(x + self.delrow[k], y + self.delcol[k]):
                        q.append((x + self.delrow[k], y + self.delcol[k], dis+1))
                        
        result = float('inf')
        
        for i in range(n):
            result = min(result, d[i][0])
            
        if result == float('inf'):
            return -1
            
        return result 
