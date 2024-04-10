# 10 April 2024
# Party of Couples

class Solution:
    def findSingle(self, n, arr):
        # code here
        arr_set = set(arr)
        temp = {i:0 for i in arr_set}
        
        for i in arr:
            temp[i] += 1
        
        for i in temp:
            if temp[i] % 2 == 1:
                return i
