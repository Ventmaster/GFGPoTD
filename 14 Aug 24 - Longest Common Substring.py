# 14th August 2024
# Longest Common Substring

class Solution:
    def longestCommonSubstr(self, str1, str2):
        # code here
        n, m = len(str1), len(str2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        result = 0
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    result = max(result, dp[i][j])
        
        return result
