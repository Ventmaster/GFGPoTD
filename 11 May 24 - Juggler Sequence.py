# 11 May 2024
# Juggler Sequence

import math

class Solution:
    def jugglerSequence(self, n):
        # code here
        result = []
        
        result.append(n)
        
        for i in range(1, n*10):
            if result[-1] % 2 != 0 and result[-1] != 1:
                x = math.floor(result[-1] ** (3/2))
                result.append(x)
                
            if result[-1] % 2 == 0 and result[-1] != 1:
                x = math.floor(result[-1] ** (1/2))
                result.append(x)
                
        return result
