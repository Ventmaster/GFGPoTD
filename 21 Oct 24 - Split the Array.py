# 21st October 2024
# Split the Array

class Solution:
    modulo = 10**9 + 7
    
    def func_modular_exponentiation(self, n):
        result = 1
        base = 2
        
        while n > 0:
            if n % 2 == 1:
                result = (result * base) % self.modulo
            
            base = (base * base) % self.modulo
            n //= 2
        
        return result
    
    def countgroup(self, arr): 
        # Complete the function
        n = len(arr)
        total_xor = 0
        
        for num in arr:
            total_xor ^= num
            
        if total_xor != 0:
            return 0
        
        return (self.func_modular_exponentiation(n - 1) - 1) % self.modulo
