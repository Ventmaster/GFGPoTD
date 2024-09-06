# 06th September 2024
# Kadane's Algorithm

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        result = arr[0]
        current = 0
        
        for i in arr:
            current += i
            result = max(current, result)
            current = max(current, 0)
            
        return result
