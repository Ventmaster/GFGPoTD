# 22 February 2024
# Distinct occurrences

from collections import defaultdict

class Solution:
    def sequenceCount(self,s, t):
        # Code here
        n, m = len(s), len(t)
        dp = defaultdict(int)
        modulo = 10**9 + 7
        
        def dfs(i, j):
            if j == m:
                return 1
            if i >= n or j >= m:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if s[i] == t[j]:    
                dp[(i, j)] += dfs(i+1, j+1)
            dp[(i, j)] += dfs(i+1, j)
            
            return dp[(i, j)] % modulo
            
        return dfs(0, 0) % modulo
