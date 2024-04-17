# 17 April 2024
# Count Pairs in an Array

from bisect import bisect_left, insort

class Solution:    
    def countPairs(self,arr, n): 
         # Your code goes here
        new_array = [i * j for i, j in enumerate(arr)]
        result = 0
        li = []
        
        for i in range(n-1, -1, -1):
            if not li:
                insort(li, new_array[i])
                continue
            
            result += bisect_left(li, new_array[i])
            insort(li, new_array[i])
            
        return result
