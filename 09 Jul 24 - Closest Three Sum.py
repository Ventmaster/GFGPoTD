# 09th July 2024
# Closest Three Sum

class Solution:
    def threeSumClosest(self, arr, target):
        # Initialize variables
        n = len(arr)
        arr.sort()
        difference = float('inf')
        result = None
        
        for i in range(n):
            first = arr[i]
            start = i + 1
            end = n - 1
            
            while start < end:
                current_sum = first + arr[start] + arr[end]
                
                if current_sum == target:
                    return target
                
                current_difference = abs(current_sum - target)
                
                if current_difference < difference or (current_difference == difference and current_sum > result):
                    difference = current_difference
                    result = current_sum
                
                if current_sum > target:
                    end -= 1
                else:
                    start += 1
        
        return result
