# 19th August 2024
# Kth Smallest

class Solution:
    def kthSmallest(self, arr,k):
        x = max(arr)
        result = [0] * (x + 1)
        
        for a in arr:
            result[a] += 1
            
        for i in range(1, x+1):
            k -= result[i]
            
            if k == 0:
                return i 
                
        return i
