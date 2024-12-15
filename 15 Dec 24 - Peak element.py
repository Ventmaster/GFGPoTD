# 15th December 2024
# Peak element

class Solution:   
    def peakElement(self,arr):
        # Code here
        n = len(arr)
        low = 0
        high = n - 1
        
        while low <= high:
            middle = (high + low) // 2
            
            if (middle == 0 or arr[middle-1] <= arr[middle]) and (middle == n-1 or arr[middle+1] <= arr[middle]):
                return middle
                
            elif arr[middle] > arr[middle+1]:
                high = middle - 1
                
            else:
                low = middle + 1
