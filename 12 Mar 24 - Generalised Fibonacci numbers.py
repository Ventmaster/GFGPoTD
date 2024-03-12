# 12 March 2024
# Generalised Fibonacci numbers

class Solution:
    def multiply_matrices(self, matrix1, matrix2, m):
        result = [[0, 0, 0] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
                    
                result[i][j] %= m
                
        return result 
        
    def exponentiate_matrix(self, matrix, exponent, m):
        identity = [[(i == j) * 1 for j in range(3)] for i in range(3)]
        
        if exponent == 0:
            return identity
            
        result = identity
        base = matrix
        
        while exponent > 0:
            if exponent % 2 == 1:
                result = self.multiply_matrices(result, base, m)
                
            exponent //= 2
            base = self.multiply_matrices(base, base, m)
            
        return result 
        
    def genFibNum(self, a, b, c, n, m):
        # code here
        if n <= 2:
            return 1 % m
            
        fib_matrix = [[a,b,c], [1,0,0], [0,0,1]]
        
        result_matrix = self.exponentiate_matrix(fib_matrix, n-2, m)
        
        return sum(result_matrix[0]) % m
