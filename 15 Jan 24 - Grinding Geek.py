# 15 January 2024
# Grinding Geek

from typing import List

class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        # code here
        dp = [0 for _ in range(total + 1)]
        
        for c in reversed(cost):
            for t in range(total, c-1, -1):
                dp[t] = max(dp[t], dp[t-(c+9)//10]+1)
        
        return dp[total]
