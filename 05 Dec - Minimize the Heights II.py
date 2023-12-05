# 05 December 2023
# Minimize the Heights II

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        
        difference = arr[n-1] - arr[0]
        
        for i in range(1, n):
            if (arr[i] - k < 0):
                continue
            
            minimum = min(arr[0] + k, arr[i] - k)
            maximum = max(arr[i-1] + k, arr[n-1] - k)
            
            difference = min(difference, maximum - minimum)
            
        result = difference
        
        return result
