# 01st November 2024
# Swap and Maximize

class Solution:
    def maxSum(self,arr):
        # code here
        n = len(arr)
        result = 0
        
        arr.sort()
        
        for i in range(n//2):
            result -= (2 * arr[i])
            result += (2 * arr[n - 1 - i])
            
        return result
