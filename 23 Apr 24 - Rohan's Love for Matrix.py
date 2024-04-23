# 23 April 2024
# Rohan's Love for Matrix

class Solution:
    def firstElement (self, n):
        # code here
        first = 1
        second = 1
        answer = 0
        
        if n <= 2:
            return first
            
        for i in range(3, n+1):
            answer = (first + second) % (10**9+7)
            first = second
            second = answer
            
        return answer
