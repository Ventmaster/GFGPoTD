# 26 April 2024
# Exit Point in a Matrix

class Solution:
    def FindExitPoint(self, n, m, matrix):
        # Code here
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        
        def solution(row, col, index):
            if row < 0 or col < 0 or row == n or col == m:
                return [row, col]
            
            if (matrix[row][col] == 1):
                index = (index + 1) % 4
                matrix[row][col] = 0
                
            return solution(row + directions[index][0], col + directions[index][1], index)
            
        result = solution(0, 0, 0)
        result[0] = max(0, min(n-1, result[0]))
        result[1] = max(0, min(m-1, result[1]))  # Added missing parentheses here
        
        return result
