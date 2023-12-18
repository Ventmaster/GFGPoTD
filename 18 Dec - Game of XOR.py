# 18 December 2023
# Game of XOR

class Solution:
    def gameOfXor(self, N , A):
        # code here 
        result = 0
        
        for i in range(N):
            if ((i+1)*(N-i)&1):
                result ^= A[i]
        
        return result
