# 15th April 2024
# Count the elements

from bisect import bisect_right

class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        b.sort()
        
        return [bisect_right(b, a[q]) for q in query]
