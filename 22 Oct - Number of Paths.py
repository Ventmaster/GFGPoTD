# 22 October 2023
# Number of Paths

class Solution:
    def numberOfPaths (self, M, N):
        # code here
        path = 1
        modulo = 10**9 + 7
        
        for _ in range(M-1):
            path = (path * (_ + N)) % modulo
            temp = pow(_+1, modulo-2, modulo)
            path = (path * temp) % modulo
            
        return path 
