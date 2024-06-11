# 11th June 2024
# Maximum Tip Calculator

from typing import List

class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        tp = zip(arr, brr)
        sorted_tips = sorted(tp, key = lambda t: abs(t[0] - t[1]), reverse = True)
        countA, countB, total = 0, 0, 0
        
        for a, b in sorted_tips:
            if (a >= b and countA < x) or countB == y:
                total += a
                countA += 1
            else:
                total += b
                countB += 1
        
        return total
