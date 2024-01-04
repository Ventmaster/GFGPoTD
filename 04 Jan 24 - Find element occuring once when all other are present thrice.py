# 04 January 2024
# Find element occuring once when all other are present thrice

class Solution:
    def singleElement(self, arr, N):
        # code here 
        d = {}
        
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for i in d:
            if d[i] == 1:
                return i 
