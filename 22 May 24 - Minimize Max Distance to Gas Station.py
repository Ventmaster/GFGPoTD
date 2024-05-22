# 22nd May 2024
# Minimize Max Distance to Gas Station

import math

class Solution:
    def findSmallestMaxDist(self, stations, K):
        # Code here
        def func(distance):
            x = 0
            
            for i in range(len(stations)-1):
                x += math.floor((stations[i+1] - stations[i])/distance)
            
            return x <= K
            
        left, right = 0, stations[-1] - stations[0]
        
        while right-left > 1e-6:
            middle = left + (right-left)/2.0
            
            if func(middle):
                right = middle
            else:
                left = middle
                
        return right
