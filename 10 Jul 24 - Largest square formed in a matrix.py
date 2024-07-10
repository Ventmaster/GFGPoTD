# 10 July 2024
# Largest square formed in a matrix

from typing import List

class Solution:
    def maxSquare(self, m : int, n : int, mat : List[List[int]]) -> int:
        # code here
        result = 0
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if mat[i][j] == 1:
                        dp[i][j] = 1
                else:
                    if mat[i][j] == 1:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                        
                
                result = max(dp[i][j], result)
        
        return result
