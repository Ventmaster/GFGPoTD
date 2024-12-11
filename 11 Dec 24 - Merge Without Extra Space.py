# 11th December 2024
# Merge Without Extra Space

class Solution:
    def mergeArrays(self, a, b):
        # code here
        n1, n2 = len(a), len(b)
        i, j = 0, 0
        k = n1 - 1
        
        while i <= k and j < n2:
            if a[i] <= b[j]:
                i += 1
                
            elif a[k] > b[j]:
                a[k], b[j] = b[j], a[k]
                j += 1
                k -= 1
                
        a.sort()
        b.sort()
