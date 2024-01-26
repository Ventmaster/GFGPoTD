# 26 January 2024
# Fractional Knapsack

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        x, y = 0, 0
        arr.sort(key = lambda a:a.value/a.weight, reverse = True)
        
        for i in arr:
            if x == W:
                break
            if (x + i.weight) <= W:
                x += i.weight
                y += i.value
            else:
                y += i.value * ((W-x)/i.weight)
                break
            
        return y
