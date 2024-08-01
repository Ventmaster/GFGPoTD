# 01 August 2024
# Spirally traversing a matrix

class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        # code here
        result = []
        
        while matrix:
            result += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
            
        return result
