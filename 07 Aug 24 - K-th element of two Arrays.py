# 07th August 2024
# K-th element of two Arrays

class Solution:
    def kthElement(self, k, arr1, arr2):
        result = arr1 + arr2
        result.sort()
        
        return result[k-1]
