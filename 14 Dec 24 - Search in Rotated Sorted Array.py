# 14th December 2024
# Search in Rotated Sorted Array

class Solution:
    def search(self,arr,key):
        # Complete this function
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            middle = (left+right)//2
            
            if arr[middle] == key:
                return middle
                
            if arr[left] <= arr[middle]:
                if arr[left] <= key < arr[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            
            else:
                if arr[middle] < key <= arr[right]:
                    left = middle + 1
                else:
                    right = middle - 1
                    
        return -1
