# 24th October 2024
# Modify the Array

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        n = len(arr)
        left, right = 0, 0
        
        for i in range(n - 2):
            if arr[i] == 0:
                continue
            
            if arr[i] == arr[i + 1]:
                arr[i] *= 2
                arr[i + 1] = 0
                
        while right < n:
            if arr[right] != 0:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                
            right += 1
            
        return arr
