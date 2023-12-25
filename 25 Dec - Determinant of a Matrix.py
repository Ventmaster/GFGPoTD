# 25 December 2023
# Determinant of a Matrix

class Solution:
    
    #Function for finding determinant of matrix.
    def determinantOfMatrix(self,matrix,n):
        # code here 
        if n == 1:
            return matrix[0][0]
            
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        result = 0
        
        for i in range(n):
            matrix1 = [matrix[j][1:] for j in range(n) if j != i]
            result += ((-1)**(i)) * matrix[i][0] * self.determinantOfMatrix(matrix1, n-1)
        
        return result
