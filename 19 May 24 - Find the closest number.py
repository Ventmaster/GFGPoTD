# 19th May 2024
# Find the closest number

from typing import List

class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        start, end = 0, n-1
        
        if n == 1:
            return arr[0]
            
        while start < end:
            middle = (start + end) // 2
            
            if arr[middle] == k:
                return k
            elif (end - start) == 1:
                difference = abs(arr[start] - k)
                if difference >= abs(arr[end] - k):
                    return arr[end]
                return arr[start]
            elif arr[middle] < k:
                start = middle
            elif arr[middle] > k:
                end = middle
