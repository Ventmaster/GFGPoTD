# 02 November 2023
# Minimum distance between two numbers

class Solution:
    def minDist(self, arr, n, x, y):
        max_x, max_y = -1, -1
        result = float('inf')
        
        for i in range(n):
            if arr[i] == x:
                max_x = max(max_x, i)
            if arr[i] == y:
                max_y = max(max_y, i)
            
            if (max_x != -1 and max_y != -1):
                result = min(result, abs(max_y - max_x))
        
        if max_x == -1 or max_y == -1:
            return -1
            
        return result 
