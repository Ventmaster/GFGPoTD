# 17th August 2024
# Product array puzzle

class Solution:
    def productExceptSelf(self, nums):
        #code here
        left, right = 1, 1
        result = [1] * len(nums)
        
        for i in range(len(nums)):
            result[i] = left
            left *= nums[i]
            
        for j in range(len(nums)-1, -1, -1):
            result[j] *= right
            right *= nums[j]
            
        return result
