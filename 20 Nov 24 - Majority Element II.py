# 20th November 2024
# Majority Element II

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        #Your Code goes here.
        hashmap = {}
        a = []
        n = len(nums) // 3
        
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
                
        for key, val in hashmap.items():
            if val > n:
                a.append(key)
                
        a.sort()
        
        return a
