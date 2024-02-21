# 22 February 2024
# Boolean Parenthesization

def countWays(self, n, s):
        # code here
        dp=[[[0,0] for _ in range(n)]for _ in range(n)]
        for i in range(0,n,2):
            if s[i]=='T':
                dp[i][i][1]=1
            else:
                dp[i][i][0]=1
        for x in range(3,n+1,2):
            for i in range(0,n-x+1,2):
                j=i+x-1
                t=(x-1)//2
                for k in range(1,t+1):
                    k2=2*k
                    if s[i+k2-1]=='&':
                        dp[i][j][1]+=dp[i][i+k2-2][1]*dp[i+k2][j][1]
                        dp[i][j][0]+=dp[i][i+k2-2][1]*dp[i+k2][j][0]+dp[i][i+k2-2][0]*dp[i+k2][j][1]+dp[i][i+k2-2][0]*dp[i+k2][j][0]
                    elif s[i+k2-1]=='|':
                        dp[i][j][0]+=dp[i][i+k2-2][0]*dp[i+k2][j][0]
                        dp[i][j][1]+=dp[i][i+k2-2][0]*dp[i+k2][j][1]+dp[i][i+k2-2][1]*dp[i+k2][j][0]+dp[i][i+k2-2][1]*dp[i+k2][j][1]
                    else:
                        dp[i][j][0]+=dp[i][i+k2-2][0]*dp[i+k2][j][0]+dp[i][i+k2-2][1]*dp[i+k2][j][1]
                        dp[i][j][1]+=dp[i][i+k2-2][1]*dp[i+k2][j][0]+dp[i][i+k2-2][0]*dp[i+k2][j][1]
        return dp[0][n-1][1]%1003
