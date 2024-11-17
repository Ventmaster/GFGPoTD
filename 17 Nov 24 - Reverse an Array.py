# 17th November 2024
# Reverse an Array

class Solution:
    def reverseArray(self, arr):
        # code here
        arr[:] = arr[::-1]
        return arr
