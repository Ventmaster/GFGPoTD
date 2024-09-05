# 05th September 2024
# Missing in Array

class Solution:
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        # code here
        Sum = n * (n+1)/2
        arr_sum = sum(arr)
        
        x = int(Sum - arr_sum)
        
        return x
