# 14 March 2024
# Largest subsquare surrounded by X

class Solution:
    def largestSubsquare(self, n, a):
        #code here
        r, c = len(a), len(a[0])
        dp = [[[0,0] for _ in range(r+1)]for _ in range(c+1)]
        
        for i in range(r):
            for j in range(c):
                if a[i][j] == 'X':
                    dp[i+1][j+1][0] = 1 + dp[i][j+1][0] 
                    dp[i+1][j+1][1] = 1 + dp[i+1][j][1]
                    
        maximum = 0
        
        for i in range(r, 0, -1):
            for j in range(c, 0, -1):
                minimum = min(dp[i][j][0], dp[i][j][1])
                
                while minimum > maximum:
                    if dp[i-minimum+1][j][1] >= minimum and dp[i][j-minimum+1][0] >= minimum:
                        maximum = minimum
                    else:
                        minimum -= 1
                        
        return maximum
