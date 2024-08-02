# 02nd August 2024
# Edit Distance

class Solution:
    def editDistance(self, str1, str3):
        # code here
        n, m = len(str1), len(str3)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                else:
                    if str1[i - 1] == str3[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[n][m]
