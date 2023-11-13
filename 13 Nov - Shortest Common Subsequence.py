# 13 November 2023
# Shortest Common Subsequence

class Solution:
    def shortestCommonSupersequence(self, str1, str2, len_str1, len_str2):
        dp = [[-1 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]

        for i in range(len_str1 + 1):
            for j in range(len_str2 + 1):
                if not i or not j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + dp[i - 1][j - 1] if str1[i - 1] == str2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])

        return len_str1 + len_str2 - dp[len_str1][len_str2]
