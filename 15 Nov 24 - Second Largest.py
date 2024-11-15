# 15th November 2024
# Second Largest

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        a = list(set(arr))
        a.sort()
        
        if len(a) <= 1:
            return -1
        else:
            return a[-2]
