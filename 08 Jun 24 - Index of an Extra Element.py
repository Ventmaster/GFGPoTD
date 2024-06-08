# 08th June 2024
# Index of an Extra Element

class Solution:
    def findExtra(self,n,a,b):
        #add code here
        arr = a + b
        xor = 0
        
        for i in range(len(arr)):
            xor ^= arr[i]
            
        for i in range(len(a)):
            if a[i] == xor:
                return i
