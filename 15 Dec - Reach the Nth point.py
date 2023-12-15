# 15 December 2023
# Reach the Nth point

class Solution:
    def nthPoint(self, n):
        # Code here
        modulo = 10**9 + 7

        if n == 0 or n == 1 or n == 2:
            return n

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % modulo

        return dp[n]
