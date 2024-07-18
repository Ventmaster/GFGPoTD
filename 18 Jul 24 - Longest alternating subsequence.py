# 18 July 2024
# Longest alternating subsequence

class Solution:
    def alternatingMaxLength(self, arr):
        # Code here
        increase, decrease = 1, 1
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                increase = decrease + 1
                
            elif arr[i] < arr[i-1]:
                decrease = increase + 1
                
        return max(increase, decrease)

