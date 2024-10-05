# 05th October 2024
# Not a subset sum

class Solution:
    def findSmallest(self, arr):
        # code here
        result = 1
        
        for i in arr:
            if i > result:
                break
            
            result += i 
            
        return result
