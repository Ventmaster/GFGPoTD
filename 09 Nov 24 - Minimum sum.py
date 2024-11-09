# 09th November 2024
# Minimum sum

from collections import Counter
from itertools import zip_longest

class Solution:
    def minSum(self, arr):
        # code here
        num1, num2 = [], []
        count = Counter(arr)
        flag = True
        
        for n in range(9, -1, -1):
            while count[n] != 0:
                if flag:
                    num1.append(n)
                else:
                    num2.append(n)
                    
                flag = not flag
                count[n] -= 1
                
        result = []
        car = 0
        
        for n1, n2 in zip_longest(num1, num2, fillvalue = 0):
            car, dig = divmod(n1+n2+car, 10)
            result.append(dig)
        
        if car:
            result.append(1)
            
        result = "".join(map(str, result[::-1]))
        
        result = result.lstrip("0")
        
        return result
