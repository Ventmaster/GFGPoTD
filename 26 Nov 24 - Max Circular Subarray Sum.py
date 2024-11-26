# 26th November 2024
# Max Circular Subarray Sum

def circularSubarraySum(arr):
    ##Your code here
    total = 0
    max_sum = curr_max = float('-inf')
    min_sum = curr_min = float('inf')
    
    for i in arr:
        curr_max = max(i, curr_max + i)
        max_sum = max(max_sum, curr_max)
        
        curr_min = min(i, curr_min + i)
        min_sum = min(min_sum, curr_min)
        
        total += i
        
    return max(max_sum, total-min_sum, total)
