# 21 July 2024
# Maximum product subset of an array

class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        modulo = 10 ** 9 + 7
        n = len(arr)
        
        if n == 1:
            return arr[0]
            
        max_neg = float('-inf')
        count_neg, count_zero = 0, 0 
        product = 1
        has_positive = False
        
        for num in arr:
            if num == 0:
                count_zero += 1
                continue
            
            if num < 0:
                count_neg += 1
                max_neg = max(max_neg, num)
            else:
                has_positive = True
                
            product *= num
            
        if count_zero == n:
            return 0
            
        if count_neg % 2 != 0:
            if count_neg == 1 and count_zero + count_neg == n:
                return 0
                
            product //= max_neg
            
        if product < 0 and has_positive:
            product = -product
            
        return product % modulo if product >= 0 else (product + modulo) % modulo
