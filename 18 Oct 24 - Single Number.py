# 18th October 2024
# Single Number

class Solution:
    def getSingle(self,arr):
        # code here
        a = arr[0]
        
        for i in arr[1:]:
            a ^= i
            
        return a
