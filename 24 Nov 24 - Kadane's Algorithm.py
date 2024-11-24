# 24th November 2024
# Kadane's Algorithm

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        result = sum = -1e9
        
        for a in arr:
            sum = max(a, sum + a)
            result = max(result, sum)
            
        return result
