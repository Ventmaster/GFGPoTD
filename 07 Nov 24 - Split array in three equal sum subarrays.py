# 07th November 2024
# Split array in three equal sum subarrays

class Solution:
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        total_sum = sum(arr)
        n = len(arr)
        current_sum = 0
        i, j = -1, -1
        
        if total_sum % 3 != 0:
            return [-1, -1]
            
        part_sum = total_sum // 3
        
        for index in range(n):
            current_sum += arr[index]
            
            if current_sum == part_sum:
                i = index
                break
            
        if i == -1:
            return [-1, -1]
            
        current_sum = 0
            
        for index in range(i + 1, n):
            current_sum += arr[index]
            
            if current_sum == part_sum:
                j = index
                break
            
        if j == -1 or j == n - 1:
            return [-1, -1]
                
        return [i, j]
