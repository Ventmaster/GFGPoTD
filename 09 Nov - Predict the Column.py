# 09 November 2023
# Predict the Column

class Solution:
    def columnWithMaxZeros(self,arr,N):
        # code here
        min_non_zero_count = float("inf")
        max_zero_col = -1
        
        for column_indice in range(N):
            zero_count = 0
            
            for row_indice in range(N):
                zero_count += arr[row_indice][column_indice]
                
            if zero_count < N and min_non_zero_count > zero_count:
                min_non_zero_count, max_zero_col = zero_count, column_indice
                
        return max_zero_col
