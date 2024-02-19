# 19 February 2024
# Game with String

import heapq
from collections import Counter

class Solution:
    def minValue(self, s, k):
        # code here
        counter = Counter(s)
        counts = [-v for v in counter.values()]
        heapq.heapify(counts)
        
        while k > 0:
            max_count = heapq.heappop(counts)
            heapq.heappush(counts, max_count+1)
            k = k - 1
            
        return sum(i**2 for i in counts)
