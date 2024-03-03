# 03 March 2024
# Largest Number formed from an Array

class Solution:
    def printLargest(self, n, arr):
        return "".join(sorted(arr, reverse = True, key = lambda _:_*18))
