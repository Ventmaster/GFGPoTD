# 08 July 2024
# Search in Rotated Sorted Array

class Solution:
    def search(self,arr,key):
        # Complete this function
        if key in arr:
            return arr.index(key)
        else:
            return -1
