# 16 January 2024
# Sequence of Sequence

class Solution:
    def numberSequence(self, m, n):
        # code here
        if m < n:
            return 0
        if n == 0:
            return 1
        return self.numberSequence(m/2, n-1) + self.numberSequence(m-1, n)
