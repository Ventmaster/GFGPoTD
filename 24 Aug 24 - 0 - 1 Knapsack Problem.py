# 24th August 2024
# 0 - 1 Knapsack Problem

class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
        # code here
        n = len(wt)
        dp = [[0 for i in range(W + 1)] for j in range(n + 1)]
        
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                j = w - wt[i-1]
                
                if j >= 0:
                    dp[i][w] = max(dp[i-1][w], (dp[i-1][j] + val[i-1]))
                else:
                    dp[i][w] = dp[i-1][w]
        
        return dp[n][W]
