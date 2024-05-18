# 17th May 2024
# Find Pair Given Difference

from typing import List

class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # code here
        arr.sort()
        Set = set()
        
        for i in reversed(arr):
            if x + i in Set:
                return 1
            Set.add(i)
            
        return -1
