# 25th August 2024
# Number of pairs

import math
import bisect

class Solution:
    #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,arr,brr):
        #code here
        n, m = len(arr), len(brr)
        a, b = []*n, []*m
        count = 0
        
        for y in arr:
            a.append(math.log(y)/y)
            
        for x in brr:
            b.append(math.log(x)/x)
            
        a.sort()
        b.sort()
        
        for i in range(m):
            index = bisect.bisect_right(a, b[i])
            count += n - index
            
        return count
