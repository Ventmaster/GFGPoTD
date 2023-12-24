# 24 December
# Buy Maximum Stocks if i stocks can be bought on i-th day

from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        result = 0
        
        for i, x in sorted(enumerate(price), key = lambda a: a[1]):
            buy = min(k // x, i + 1)
            
            if buy == 0:
                break
            
            result = result + buy
            
            k = k - buy * x 
            
        return result
