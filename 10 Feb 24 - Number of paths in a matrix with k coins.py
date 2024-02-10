# 10 February 2024
# Number of paths in a matrix with k coins

class Solution:
    def numberOfPath (self, n, k, arr):
        # code here
        def func(i, j, k):
            if i == n-1 and j == n-1 and k == arr[i][j]:
                return 1
            if i >= n or j >= n or k < 0:
                return 0
            if dp[i][j][k] != -1:
                return dp[i][j][k]
                
            down = func(i+1, j, k-arr[i][j])
            right = func(i, j+1, k - arr[i][j])
            
            dp[i][j][k] = down + right
            
            return dp[i][j][k]
            
        dp = [[[-1 for _ in range(k+1)]for _ in range(n+1)] for _ in range(n+1)]
        
        return func(0, 0, k)
