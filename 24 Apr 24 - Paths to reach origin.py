# 24 April 2024
# Paths to reach origin

class Solution:
    def ways(self, n,m):
        #write you code here
        modulo = 10**9 + 7
        x = min(n, m)
        
        num = n + m
        p, q = 1, 1
        
        for i in range(1, x+1):
            p *= num
            num -= 1
            q *= i
            
        return (p // q) % modulo
