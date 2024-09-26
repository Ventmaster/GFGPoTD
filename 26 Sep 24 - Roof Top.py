# 26th September 2024
# Roof Top

class Solution:
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        result = 0
        current = 0
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                current += 1
                result = max(result, current)
            else:
                current = 0
                
        return result
