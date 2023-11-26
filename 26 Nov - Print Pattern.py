# 26 November 2023
# Print Pattern

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def __init__(self):
        self.li = []
    def pattern(self, N):
        # code here
        self.li.append(N)
        
        if (N > 0):
            self.pattern(N-5)
            self.li.append(N)
        
        return self.li
