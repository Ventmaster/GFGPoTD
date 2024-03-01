# 01 March 2024
# Peak element

class Solution:   
    def peakElement(self,arr, n):
        # Code here
        maximum = max(arr)
        j = 0
        
        for i in arr:
            j += 1
            
            if i == maximum:
                break
            
        return j - 1
