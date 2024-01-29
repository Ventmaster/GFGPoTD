# 29 January 2024
# Count digit groupings of a number

from functools import lru_cache

class Solution:
    def TotalCount(self, s):
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = int(s[j])
                else:
                    dp[i][j] = dp[i][j-1] + int(s[j])
                    
        @lru_cache(None)
        def util(previous_n, i):
            if i == n:
                return 1
            
            answer = 0
            
            for x in range(i, n):
                if dp[i][x] >= previous_n:
                    answer += util(dp[i][x], x+1)
                    
            return answer
        
        return util(0, 0)
