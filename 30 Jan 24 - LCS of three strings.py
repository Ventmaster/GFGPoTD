# 30 January 2024
# LCS of three strings

class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        # code here
        dp = [[[0 for _ in range(n3+1)]for _ in range(n2+1)]for _ in range(n1+1)]
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                for k in range(1, n3+1):
                    if A[i-1] == B[j-1] and B[j-1] == C[k-1]:
                        dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
                        
        return dp[-1][-1][-1]
