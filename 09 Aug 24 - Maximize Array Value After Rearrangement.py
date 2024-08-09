# 09th August 2024
# Maximize Array Value After Rearrangement

class Solution:
    def Maximize(self, a): 
        # Complete the function
        arr = sorted(a)
        modulo = 10**9 + 7
        sum = 0
        
        for i in range(len(arr)):
            sum += i * arr[i]
            
        return sum % modulo
