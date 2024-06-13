# 13th June 2024
# Padovan Sequence

class Solution:
    modulo = 10**9 + 7
    def padovanSequence(self, n):
        # code here 
        a,b,c = 1,1,1
        
        for i in range(3, n+1):
            a,b,c = b,c,(a+b)%self.modulo
            
        return c
