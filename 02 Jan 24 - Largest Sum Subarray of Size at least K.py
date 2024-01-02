# 02 January 2024
# Largest Sum Subarray of Size at least K

class Solution():
    def maxSumWithK(self, a, n, k):
        # Code here
        sum = 0
        last = 0
        j = 0
        result = float('-inf')
        
        for i in range(k):
            sum = sum + a[i]
        
        result = max(result, sum)
        
        for i in range(k, n):
            sum += a[i]
            last += a[j]
            
            j += 1
            result = max(result, sum)
            
            if (last < 0):
                sum -= last
                result = max(result, sum)
                last = 0
                
        return result
