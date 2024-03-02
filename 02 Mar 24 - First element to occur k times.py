# 02 March 2024
# First element to occur k times

from collections import defaultdict

class Solution:
    def firstElementKTime(self, n, k, a):
        # code here
        temporary = defaultdict(int)
        
        for i in a:
            temporary[i] += 1
            
            if temporary[i] == k:
                return i 
                
        return -1
