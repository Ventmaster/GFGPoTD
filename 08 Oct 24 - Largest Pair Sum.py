# 08th October 2024
# Largest Pair Sum

from typing import List

class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here
        x = y = float('-inf')
        
        for n in arr:
            if n > x:
                y = x
                x = n
            elif n > y:
                y = n
                
        return x + y
