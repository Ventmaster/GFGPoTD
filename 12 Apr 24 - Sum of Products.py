# 12 April 2024
# Sum of Products

class Solution:
    def pairAndSum(self, n, arr):
        #code here
        sop = 0
        
        for i in range(32):
            count = 0
            
            for j in arr:
                if j & (1 << i):
                    count += 1
                    
            sop += count * (count - 1) // 2 * (1 << i)
            
        return sop
