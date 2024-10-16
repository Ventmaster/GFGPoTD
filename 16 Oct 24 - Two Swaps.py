# 16th October 2024
# Two Swaps

class Solution:
    def checkSorted(self, arr):
        #code here
        n = 2
        i = 0
        end = len(arr)
        
        while i < end:
            if arr[i] != (i + 1):
                if n < 1:
                    return False
                    
                n -= 1
                
                temp = arr[arr[i] - 1]
                arr[arr[i] - 1] = arr[i]
                arr[i] = temp
            
            else:
                i += 1
                
        if n == 1:
            return False
            
        return True
