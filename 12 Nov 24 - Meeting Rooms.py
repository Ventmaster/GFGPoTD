# 12th November 2024
# Meeting Rooms

class Solution:
    def canAttend(self,arr):
        # Your Code Here
        start = arr[0][0]
        end = arr[0][1]
        arr.sort()
        
        for i in range(1, len(arr)):
            if arr[i][0] >= end:
                end = arr[i][1]
            else:
                return False
        
        return True
