# 27th May 2024
# Longest subsequence-1

from typing import List

class Solution:
    def longestSubseq(self, n : int, a : List[int]) -> int:
        # code here
        ans, dp = 0, [0]*n
        
        for i in range(1, n):
            for j in range(0, i):
                if abs(a[i]-a[j]) == 1:
                    dp[i] = max(dp[i], dp[j]+1)
                    
            ans = max(ans, dp[i])
            
        return ans+1
