# 16th August 2024
# Maximize The Cut Segments

from sys import setrecursionlimit
from functools import lru_cache

class Solution:
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        x, y, z = sorted([x, y, z])
        
        if n % x == 0:
            return n // x
            
        setrecursionlimit(5*10**3)
        @lru_cache(None)
        
        def dfs(current = n):
            nonlocal x,y,z
            
            if current == 0:
                return 0
                
            if current < 0:
                return -float('inf')
            
            return max(dfs(current - x), dfs(current - y), dfs(current - z)) + 1
            
        result = dfs()
        
        return result if result != -float('inf') else 0
