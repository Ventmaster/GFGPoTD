# 12th August 2024
# Sum of Middle elements of two sorted arrays

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        arr1.extend(arr2)
        arr1.sort()
        
        n = len(arr1)
        
        if n % 2 == 0:
            return arr1[n // 2] + arr1[(n//2) - 1]
        elif n % 2 != 0:
            return arr1[n // 2]
            
        return -1
