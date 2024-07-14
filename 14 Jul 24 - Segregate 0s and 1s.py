# 14th July 2024
# Segregate 0s and 1s

class Solution:
    def segregate0and1(self, arr):
        left = 0
        for right in range(len(arr)):
            if arr[right] == 0:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
