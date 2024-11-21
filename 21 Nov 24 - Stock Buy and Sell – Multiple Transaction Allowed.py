# 21st November 2024
# Stock Buy and Sell – Multiple Transaction Allowed

from typing import List

class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        result = 0
        n = len(prices)
        
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                result += arr[i] - arr[i-1]
                
        return result
