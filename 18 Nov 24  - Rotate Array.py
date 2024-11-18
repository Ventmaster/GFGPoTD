# 18th November 2024
# Rotate Array

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        d %= len(arr)
        
        def rotate(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
                
        rotate(arr, 0, d - 1)
        rotate(arr, d, len(arr) - 1)
        rotate(arr, 0, len(arr) - 1)
        
        return arr
