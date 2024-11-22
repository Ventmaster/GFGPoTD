# 27th November 2024
# Stock Buy and Sell – Max one Transaction Allowed

class Solution:
    def maximumProfit(self, prices):
        # code here
        buy = prices[0]
        result = 0
        
        for i in prices[1:]:
            if i < buy:
                buy = i
            else:
                result = max(result, i-buy)
                
        return result
