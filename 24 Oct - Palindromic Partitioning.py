# 24 October 2023
# Palindrome Partitioning

from collections import defaultdict
from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def palindromicPartition(self, string):
        # code here
        d = defaultdict(set)
        n = len(string)
        
        def help(i, j):
            while i >= 0 and j < n and string[i] == string[j]:
                d[i].add(j)
                i = i - 1
                j = j + 1
                
        for k in range(n):
            help(k, k)
            help(k, k+1)
            
        @lru_cache()
        
        def dp(i):
            if i == -1:
                return 0
            return min([dp(k-1)+1 for k in range(0, i+1) if i in d[k]])
            
        return dp(n-1) - 1
