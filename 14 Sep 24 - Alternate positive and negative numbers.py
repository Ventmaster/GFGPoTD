# 14th September 2024
# Alternate positive and negative numbers

class Solution:
    def rearrange(self,arr):
        # code here
        a, b = [], []
        i, j = 0, 0
        
        for k in range(len(arr)):
            if arr[k] < 0:
                a.append(arr[k])
            if arr[k] >= 0:
                b.append(arr[k])
                
        arr.clear()
        
        while i < len(b) or j < len(a):
            if i < len(b):
                arr.append(b[i])
                i += 1
            if j < len(a):
                arr.append(a[j])
                j += 1
