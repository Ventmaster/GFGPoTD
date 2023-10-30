# 30 October 2023
# Sum of XOR of all pairs

class Solution:
    def sumXOR (self, arr, n) : 
        #Complete the function
        result = 0
        
        for i in range(32):
            ones = 0
            
            for x in arr:
                ones = ones + (1 if (x & (1 << i)) else 0)
                
            result += (ones * (n - ones) * (1 << i))
            
        return result 
