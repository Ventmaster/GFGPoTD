# 27 October 2023
# Minimum Deletions

class Solution:
    def minimumNumberOfDeletions(self,S):
        # code here
        n = len(S)
        result = [[0 for i in range(n)] for j in range(n)]
        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if S[i] == S[j]:
                    result[i][j] = result[i+1][j-1]
                else:
                    result[i][j] = min(result[i+1][j], result[i][j-1])+1
                    
        return result[0][n-1]
