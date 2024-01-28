# 28 January 2024
# Geekina Hate 1s

from typing import List
from math import log2, factorial

class Solution:
    def combination(self, n, r):
        return factorial(n)//(factorial(r)*factorial(n-r)) if n >= r else 0
    
    def count_exact(self, a, k):
        if k == 0:
            return 1
        if a == 0:
            return 0
        
        m = int(log2(a))
        
        if m < k-1:
            return 0
        return self.combination(m,k) + self.count_exact(a^(1<<m), k-1)
        
    def count(self, a, k):
        return sum(self.count_exact(a, i) for i in range(k+1))
    
    def findNthNumber(self, n : int, k : int ) -> int:
        # code here
        low = 0
        high = 10**18
        
        while low < high:
            middle = low + (high - low)//2
            
            if self.count(middle, k) >= n:
                high = middle
            else:
                low = middle + 1
                
        return low
