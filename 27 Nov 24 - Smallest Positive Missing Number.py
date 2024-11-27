# 27th November 2024
# Smallest Positive Missing Number

class Solution:
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        visited = set(arr)
        i = 1
        
        while (i in visited):
            i += 1
            
        return i
