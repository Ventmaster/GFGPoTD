# 05th June 2024
# Swapping pairs make sum equal

class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        difference = sum(a) - sum(b)
        Set = set(a)
        
        if difference % 2 != 0:
            return -1
            
        target = difference // 2
        
        for i in b:
            if (i + target) in Set:
                return 1
                
        return -1
