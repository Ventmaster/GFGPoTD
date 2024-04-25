# 25 April 2024
# Maximum sum of hour glass

class Solution:
    def findMaxSum(self,n,m,mat):
        #code here
        if n >= 3 and m >= 3:
            a,b,c = 0, 0, 0
            result = 0
            
            for i in range(2, n):
                for j in range(2, m):
                    a = mat[i-2][j-2] + mat[i-2][j-1] + mat[i-2][j]
                    b = mat[i-1][j-1]
                    c = mat[i][j] + mat[i][j-1] + mat[i][j-2]
                    
                    result = max(result, a+b+c)
                    
            return result
            
        return -1
