# 27 December 2023
# Anti Diagonal Traversal of Matrix

class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        capacity = n ** 2
        i, j = 0, 0
        traversed = 0
        answer = []
        
        while traversed < capacity:
            if j == n:
                j -= 1
                i += 1
            temp_i = i
            temp_j = j
            
            while temp_i >= 0 and temp_j >= 0 and temp_i < n and temp_j < n:
                answer.append(matrix[temp_i][temp_j])
                traversed += 1
                temp_i += 1
                temp_j -= 1
            
            j += 1
            
        return answer
