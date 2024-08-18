# 18th August 2024
# Split an array into two equal Sum subarrays

class Solution:
    def canSplit(self, arr):
        # code here
        sum1, sum2 = sum(arr), 0
        
        for x in arr:
            if sum2 == sum1:
                return True
            
            elif sum2 < sum1:
                sum1 -= x
                sum2 += x
                
            else:
                return False
