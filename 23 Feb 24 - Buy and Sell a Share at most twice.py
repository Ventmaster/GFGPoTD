# 23 February 2024
# Buy and Sell a Share at most twice

from typing import List

class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        arr = [0] * n
        maximum = price[-1]
        result = 0
        
        for i in range(n-1, -1, -1):
            if price[i] > maximum:
                maximum = price[i]
            else:    
                result = max(result, maximum - price[i])
                arr[i] = result
                
        minimum = price[0]
        new_result = 0
        num = [0] * n
        
        for i in range(n):
            if price[i] < minimum:
                minimum = price[i]
            else:
                new_result = max(price[i]-minimum, new_result)
                num[i] = new_result
                
        x = max(num[-1], arr[0])
        
        for i in range(n-1):
            x = max(x, num[i] + arr[i+1])
            
        return x
