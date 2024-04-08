# 08 April 2024
# Optimal Strategy For A Game

import sys
sys.setrecursionlimit(10**7)

#Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self,n, arr):
        # code here
        def func(i, j, s):
            if i > j:
                return 0
            if i == j:
                return arr[i]
            if (i, j) in dp:
                return dp[(i,j)]
            
            x = arr[j] + s - arr[j] - func(i, j-1, s - arr[j])
            y = arr[i] + s - arr[i] - func(i+1, j, s - arr[i])
            
            dp[(i,j)] = max(x, y)
            return dp[(i, j)]
            
        dp = {}
        s = sum(arr)
        
        return func(0, n-1, s)
