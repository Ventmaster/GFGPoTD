# 12 February 2024
# Recursive sequence

class Solution:
    def sequence(self, n):
        # code here
        if n == 1:
            return 1
            
        modulo = 10**9 + 7
        add, temp = 0, 1
        
        for i in range(n):
            multi = 1
            
            for j in range(i+1):
                multi = (multi * temp) % modulo
                temp += 1
                
            add = (add + multi) % modulo
            
        return add % modulo
