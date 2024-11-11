# 11th November 2024
# Make array elements unique

class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        inc = 0
        
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                inc += (arr[i-1] + 1 - arr[i])
                arr[i] = arr[i-1] + 1
        
        return inc
