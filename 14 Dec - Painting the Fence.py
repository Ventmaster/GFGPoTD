# 14 December 2023
# Painting the Fence

class Solution:
    def countWays(self, n, k):
        #code here.
        dp = [k, k**2, k**3-k] + [0]*(n-3)
        modulo = 10**9 + 7

        for i in range(3, n):
            dp[i] = (k * dp[i-1] - (k-1) * dp[i-3]) % modulo

        return dp[n-1]
