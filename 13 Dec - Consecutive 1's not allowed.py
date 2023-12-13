# 13 December 2023
# Consecutive 1's not allowed

class Solution:
    def countStrings(self, n):
        #code here
        modulo = 10**9 + 7

        prev, curr = 1, 2

        for i in range(2, n+1):
            prev, curr = curr, (prev+curr)%modulo

        return curr
