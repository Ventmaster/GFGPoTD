# 03rd October 2024
# Majority Vote

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        #Your Code goes here.
        onethird = len(nums) / 3
        d = {}
        result = []
        
        for i in nums:
            if i not in d:
                d[i] = 0
                
            d[i] += 1
            
        del nums
        
        for key, val in d.items():
            if val > onethird:
                result.append(key)
                
        del d
        
        return result if result else [-1]
