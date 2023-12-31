# 31 December 2023
# New Year Resolution

from typing import List


class Solution:
    def isPossible(self, n : int, coins : List[int]) -> bool:
        # code here
        # using dp 
        
        sumi = sum(coins)
        if sumi < 20:
            return False
        if sumi == 2024 :
            return True
        dp = [[0 for i in range(sumi+1)] for j in range(len(coins)+1)]
        
        for j in range(sumi+1):
            dp[0][j] = False
        for i in range(len(coins)+1):
            dp[i][0] = True
        
        for i in range(1, len(coins)+1):
            for j in range(1, sumi+1):
                if j - coins[i-1] >= 0:
                    dp [i][j] = dp[i-1][j] or dp[i-1][j - coins[i-1]] 
                else:
                    dp[i][j] = dp[i-1][j] 
        # print(dp)
        for i in range (1, len(coins)+1) :
            for j  in range(20, sumi + 1, 20):
                if dp[i][j] :
                    return 1
        
        for i in range (len(coins)+1) :
            for j in range(24, sumi + 1 , 24):
                if dp[i][j] :
                    return 1
        return 0
