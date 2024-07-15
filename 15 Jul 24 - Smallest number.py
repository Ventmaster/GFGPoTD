# 15th July 2024
# Smallest number

class Solution:
    def smallestNumber(self, s, d):
        # code here
        def func(n):
            result = 0
            
            while n > 0:
                result += (n % 10)
                n //= 10
                
            return result
            
        minimum = 10 ** (d - 1)
        maximum = 10 ** d
        
        for i in range(minimum, maximum):
            if s == func(i):
                return i
                
        return -1
