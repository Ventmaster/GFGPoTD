# 25 November 2023
# Shuffle Integers

class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        middle = n // 2
        
        i, j = 1, middle
        
        while j < n:
            arr.insert(i, arr[j])
            arr.pop(j+1)
            j = j + 1
            i = i + 2
            
        return arr
