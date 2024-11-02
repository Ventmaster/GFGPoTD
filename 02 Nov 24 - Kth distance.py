# 02nd November 2024
# Kth distance

class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        x = 0
        
        for i in range(len(arr) - 1):
            if arr[i] in arr[i+1:i+k+1]:
                x = 1
                break
            
        if x == 1:
            return True
        else:
            return False
