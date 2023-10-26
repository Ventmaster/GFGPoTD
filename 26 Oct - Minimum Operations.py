# 26 October 2023
# Minimum Operations

class Solution:
    def minOperation(self, n):
        # code here
        x = 0 
        
        while n > 0:
            if n % 2 == 0:
                n //= 2
                x += 1
            elif n % 2 != 0:
                n -= 1
                x += 1
            elif n == 0:
                break
            
        return x
