# 06 November 2023
# Letters Collection

class Solution:
    def matrixSum(self, n, m, mat, q, queries):
        # code here
        li1 = []
        
        while q > 0:
            q -= 1
            sum1 = 0
            
            hop = queries[q][0]
            i = queries[q][1]
            j = queries[q][2]
            li2 = []
            
            if hop == 1:
                li2 = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j+1),(i+1,j+1),(i+1,j),(i+1,j-1),(i,j-1)]
            
            if hop == 2:
                li2 = [(i-2,j-2),(i-2,j-1),(i-2,j),(i-2,j+1),(i-2,j+2),(i-1,j+2),(i,j+2),(i+1,j+2),(i+2,j+2),(i+2,j+1),(i+2,j),(i+2,j-1),(i+2,j-2),(i+1,j-2),(i,j-2),(i-1,j-2)]
                
            for i, j in li2:
                if i < 0 or j < 0 or i > n-1 or j > m-1:
                    sum1 += 0
                else:
                    sum1 += mat[i][j]
            
            li1.append(sum1)
            
        li1.reverse()
        return li1
