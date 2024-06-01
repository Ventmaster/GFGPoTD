# 01st June 2024
# Odd Even Problem

class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        d = {}
        
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        x = y = 0
        
        for i in d:
            if ord(i) % 2 == 0 and d[i] % 2 == 0:
                y += 1
            elif ord(i) % 2 != 0 and d[i] % 2 != 0:
                x += 1
                
        return 'EVEN' if (x + y) % 2 == 0 else 'ODD'
