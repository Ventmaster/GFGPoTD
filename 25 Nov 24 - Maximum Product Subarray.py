# 25th November 2024
# Maximum Product Subarray

class Solution:
    def maxProduct(self, arr):
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]
        
        for i in range(1, len(arr)):
            num = arr[i]
            
            if num < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            
            result = max(result, max_product)
        
        return result
