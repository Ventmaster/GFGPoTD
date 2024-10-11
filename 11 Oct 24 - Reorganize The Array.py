# 11th October 2024
# Reorganize The Array

class Solution:
    def rearrange(self, arr):
        #Code here
        for i in range(len(arr)):
            while arr[i] != i and arr[i] != -1:
                temp = arr[arr[i]]
                arr[arr[i]] = arr[i]
                arr[i] = temp
                
        return arr
