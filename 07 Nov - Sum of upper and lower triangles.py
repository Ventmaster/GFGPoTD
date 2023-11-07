# 07 November 2023
# Sum of upper and lower triangles

class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        # code here
        val1 = 0
        val2 = 0
        
        for i in range(n):
            for j in range(i, n):
                val1 += matrix[i][j]
            for k in range(i+1):
                val2 += matrix[i][k]
        
        return val1, val2
