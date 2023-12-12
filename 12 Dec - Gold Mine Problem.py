# 12 December 2023
# Gold Mine Problem

class Solution:
    def maxGold(self, n, m, mine):
        dp = [[mine[i][j] for j in range(m)] for i in range(n)]
        for j in range(m - 2, -1, -1):
            for i in range(n):
                mu = dp[i - 1][j + 1] if i - 1 >= 0 else 0
                mr = dp[i][j + 1]
                md = dp[i + 1][j + 1] if i + 1 < n else 0
                dp[i][j] += max(mu, mr, md)
        
        return max(dp[i][0] for i in range(n))
