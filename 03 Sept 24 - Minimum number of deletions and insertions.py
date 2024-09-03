# 03rd September 2024
# Minimum number of deletions and insertions

class Solution:
    def minOperations(self, str1, str2):
        n, m = len(str2), len(str1)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, m + 1):
            dp[0][i] = i

        for i in range(1, n + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[j - 1] == str2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1

        return dp[n][m]
