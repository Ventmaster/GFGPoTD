# 29th May 2024
# Geek and its Game of Coins

class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        # code here
        dp = [False] * (n+1)
        
        for i in range(1, len(dp)):
            a = i - 1
            b = i - x
            c = i - y
            result = dp[a]
            
            if b >= 0:
                result = result and dp[b]
            if c >= 0:
                result = result and dp[c]
                
            dp[i] = not result
            
        return int(dp[-1])
