# 25 February 2024
# Reach a given score

class Solution:
    def count(self, n: int) -> int:
        #your code here
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in [3, 5, 10]:
            for j in range(i, n+1):
                dp[j] += dp[j-i]
                
        return dp[n]
