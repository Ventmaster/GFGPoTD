# 18 April 2024
# Two Repeated Elements

import math

class Solution:
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        #Your code here
        sum1, sum2 = 0, 0
        
        for i in range(len(arr)):
            sum1 += arr[i]
            sum2 += (arr[i] * arr[i])
            
        k = sum1 - ((n * (n + 1)) // 2)
        c = sum2 - ((n * (n + 1) * (2 * n + 1)) // 6)
        
        x = (k + math.floor(pow((2 * c - (k * k)), 0.5))) // 2
        y = (k - math.floor(pow((2 * c - (k * k)), 0.5))) // 2
        
        count1, count2 = 0, 0
        
        for i in range(len(arr)):
            if arr[i] == x:
                if count1 == 1:
                    return [x, y]
                
                count1 += 1
            
            elif arr[i] == y:
                if count2 == 1:
                    return [y, x]
                
                count2 += 1
                
        return [-1, -1]
