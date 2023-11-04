# 04 November 2023
# Find Transition Point

class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        left = 0
        right = n-1
        result = -1
        
        while (left <= right):
            middle = (left + right) // 2
            
            if arr[middle] == 1:
                right = middle - 1
                result = middle
            elif arr[middle] == 0:
                left = middle + 1
                
        return result
