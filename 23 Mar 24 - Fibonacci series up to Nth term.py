# 23 March 2024
# Fibonacci series up to Nth term

class Solution:
    def series(self, n):
        # Code here
        dp = [0, 1]
        
        for i in range(2, n+1):
            x = dp[-1] + dp[-2]
            dp.append(x % (10**9+7))
            
        return dp
