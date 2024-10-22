# 22nd October 2024
# Sub-arrays with equal number of occurences

class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        d = {}
        pre, ans = 0, 0
        
        for i in range(len(arr)):
            if arr[i] == x:
                pre += x
                
            if arr[i] == y:
                pre += -x
                
            if pre == 0:
                ans += 1
                
            if pre in d:
                ans += d[pre]
                
            d[pre] = d.get(pre, 0) + 1
            
        return ans
