# 17 February 2024
# Does array represent Heap

class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here
        for i in range(n):
            if ((2*i+1<n and arr[i] < arr[2*i+1]) or (2*i+2<n and arr[i] < arr[2*i+2])):
                return 0
                
        return 1
