# 02nd October 2024
# Rotate and delete

class Solution:
    def rotateDelete(self,  arr):
        # code here
        n = len(arr)
        
        for k in range(1, n//2 + 1):
            arr.insert(0, arr.pop())
            arr.pop(-k)
        
        return arr[0]
