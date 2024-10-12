# 12th October 2024
# Two Smallests in Every Subarray

class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        n = len(arr)
        result = 0
        
        if n < 2:
            return -1
            
        for i in range(1, n):
            result = max(result, arr[i] + arr[i-1])
        
        return result
