# 26th October 2024
# Alternative Sorting

class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        result = []
        a = len(arr)
        b = a//2
        
        arr.sort()
        
        for i in range(b):
            result.append(arr[a - i - 1])
            result.append(arr[i])
            
        if a % 2 == 1:
            result.append(arr[b])
            
        return result
