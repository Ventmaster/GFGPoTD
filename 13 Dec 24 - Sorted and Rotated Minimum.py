# 13th December 2024
# Sorted and Rotated Minimum

class Solution:
    def findMin(self, arr):
        #complete the function here
        left, right = 0, len(arr) - 1
        
        while left < right:
            middle = (left + right) // 2
            
            if arr[middle] > arr[right]:
                left = middle + 1
            else:
                right = middle
                
        return arr[left]
