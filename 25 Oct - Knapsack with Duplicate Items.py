# 25 October 2023
# Knapsack with Duplicate Items

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        li = [[0]*(W+1)] * (N+1)
        
        for i in range(N+1):
            for j in range(W+1):
                if i == 0 or j == 0:
                    li[i][j] = 0
                    continue
                
                if wt[i-1] <= j:
                    li[i][j] = max(val[i-1] + li[i][j-wt[i-1]], li[i-1][j])
                else:
                    li[i][j] = li[i-1][j]
                    
        return li[N][W]
